from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import UserCreate, UserRead
from db.dals import UserDAL
from db.session import get_db

user_router = APIRouter(prefix="/users", tags=["users"])

async def _create_new_user(body: UserCreate, db) -> UserRead:
    async with db as session:
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
async def create_user(body: UserCreate, db: AsyncSession = Depends(get_db)) -> UserRead:
    return await _create_new_user(body, db)