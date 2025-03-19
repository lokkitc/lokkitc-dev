from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import settings
from sqlalchemy.dialects.postgresql import UUID
import uuid
import re
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, field_validator
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean


engine = create_async_engine(settings.REAL_DATABASE_URL, echo=True, future=True)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    surname: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)


class UserDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(self, name: str, surname: str, email: EmailStr) -> User:
        new_user = User(
            name=name,
            surname=surname,
            email=email
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user
    

LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z]+$")



class TunedModel(BaseModel):
    class Config:
        from_attributes = True


class UserRead(TunedModel):
    user_id: uuid.UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool

class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr

    @field_validator("name", "surname", mode="before")
    def validate_name(cls, v):
        if not LETTER_MATCH_PATTERN.match(v):
            raise HTTPException(
                status_code=422,
                detail="Must contain only letters"
            )
        return v


app = FastAPI(title="LokkitCDev API")

user_router = APIRouter(prefix="/users", tags=["users"])

async def _create_new_user(body: UserCreate) -> UserRead:
    async with async_session() as session:
        async with session.begin():
            user_dal = UserDAL(session)
            new_user = await user_dal.create_user(
                name=body.name,
                surname=body.surname,
                email=body.email
            )
            return UserRead(
                user_id=new_user.user_id,
                name=new_user.name,
                surname=new_user.surname,
                email=new_user.email,
                is_active=new_user.is_active    
            )
        

@user_router.post("/", response_model=UserRead)
async def create_user(body: UserCreate) -> UserRead:
    return await _create_new_user(body)

main_api_router = APIRouter()

main_api_router.include_router(user_router)

app.include_router(main_api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

