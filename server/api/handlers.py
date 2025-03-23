from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import UserCreate, UserRead, UserDeleteResponse, UpdateUserResponse
from db.dals import UserDAL
from db.session import get_db

from fastapi import HTTPException
from uuid import UUID
from typing import Union

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
        
async def _delete_user(user_id, db) -> Union[UUID, None]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            deleted_user_id = await user_dal.delete_user(
                user_id=user_id
            )
            return deleted_user_id


@user_router.post("/", response_model=UserRead)
async def create_user(body: UserCreate, db: AsyncSession = Depends(get_db)) -> UserRead:
    return await _create_new_user(body, db)

@user_router.delete("/{user_id}", response_model=UserDeleteResponse)
async def delete_user(user_id: UUID, db: AsyncSession = Depends(get_db)) -> UserDeleteResponse:
    deleted_user_id = await _delete_user(user_id, db)
    if deleted_user_id is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserDeleteResponse(user_id=deleted_user_id)

