from fastapi import HTTPException
from uuid import UUID
from typing import Union

from schemas.users import UserCreate, UserRead, UserUpdateRequest
from db.dals import UserDAL
from core.hashing import Hasher

async def create_new_user(body: UserCreate, session) -> UserRead:
    async with session.begin():
        user_dal = UserDAL(session)
        new_user = await user_dal.create_user(
            name=body.name,
            surname=body.surname,
            email=body.email,
            hashed_password=Hasher.get_password_hash(body.password),
            username=body.username,
        )
        return UserRead(
            user_id=new_user.user_id,
            name=new_user.name,
            surname=new_user.surname,
            email=new_user.email,
            is_active=new_user.is_active,
            username=new_user.username,
            photo=new_user.photo
        )

async def delete_user(user_id, session) -> Union[UUID, None]:
    async with session.begin():
        user_dal = UserDAL(session)
        deleted_user_id = await user_dal.delete_user(
            user_id=user_id
        )
        return deleted_user_id

async def get_user(user_id, session) -> Union[UserRead, None]:
    async with session.begin():
        user_dal = UserDAL(session)
        user = await user_dal.get_user(user_id=user_id)
        if user is not None:
            return UserRead(
                user_id=user.user_id,
                name=user.name,
                surname=user.surname,
                email=user.email,
                is_active=user.is_active,
                username=user.username,
                photo=user.photo
            )
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

async def get_users(session) -> list[UserRead]:
    async with session.begin():
        user_dal = UserDAL(session)
        users = await user_dal.get_users()
        return [UserRead(
            user_id=user.user_id,
            name=user.name,
            surname=user.surname,
            email=user.email,
            is_active=user.is_active,
            username=user.username,
            photo=user.photo
            ) for user in users]

async def update_user(updated_user_params: dict, user_id: UUID, session) -> Union[UUID, None]:
    async with session.begin():
        user_dal = UserDAL(session)
        print(f"Updating user with params: {updated_user_params}") 
        result = await user_dal.update_user(
            user_id=user_id,
            **updated_user_params
        )
        await session.commit() 
        return user_id 