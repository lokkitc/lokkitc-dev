from fastapi import HTTPException
from uuid import UUID
from typing import Union
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from schemas.users import UserCreate, UserRead, UserUpdateRequest
from db.dals.user_dal import UserDAL
from db.models.users import User, UserRole
from core.hashing import Hasher

async def create_new_user(body: UserCreate, session) -> UserRead:
    async with session.begin():
        user_dal = UserDAL(session)
        new_user = await user_dal.create_user(
            name=body.name,
            surname=body.surname,
            email=body.email,
            hashed_password=Hasher.get_password_hash(body.password),
            roles=[UserRole.ROLE_USER,],
            username=body.username,
        )
        return UserRead(
            user_id=new_user.user_id,
            name=new_user.name,
            surname=new_user.surname,
            email=new_user.email,
            is_active=new_user.is_active,
            username=new_user.username,
            photo=new_user.photo,
            header_photo=new_user.header_photo,
            frame_photo=new_user.frame_photo,
            about=new_user.about,
            location=new_user.location,
            age=new_user.age,
            created_at=new_user.created_at,
            updated_at=new_user.updated_at
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
                photo=user.photo,
                header_photo=user.header_photo,
                frame_photo=user.frame_photo,
                about=user.about,
                location=user.location,
                age=user.age,
                created_at=user.created_at,
                updated_at=user.updated_at
            )
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

async def get_user_by_username(username, session) -> Union[UserRead, None]:
    async with session.begin():
        user_dal = UserDAL(session)
        user = await user_dal.get_user_by_username(username=username)
        if user is not None:
            return UserRead(
                user_id=user.user_id,
                name=user.name,
                surname=user.surname,
                email=user.email,
                is_active=user.is_active,
                username=user.username,
                photo=user.photo,
                header_photo=user.header_photo,
                frame_photo=user.frame_photo,
                about=user.about,
                location=user.location,
                age=user.age,
                created_at=user.created_at,
                updated_at=user.updated_at
            )
        raise HTTPException(status_code=404, detail=f"User with username {username} not found")

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
            photo=user.photo,
            header_photo=user.header_photo,
            about=user.about,
            location=user.location,
            age=user.age,
            created_at=user.created_at,
            updated_at=user.updated_at
            ) for user in users]

def check_user_permissions(target_user: User, current_user: User) -> bool:
     if target_user.user_id != current_user.user_id:
         if not {
             UserRole.ROLE_ADMIN,
             UserRole.ROLE_SUPERADMIN,
         }.intersection(current_user.roles):
             return False
         if (
             UserRole.ROLE_SUPERADMIN in target_user.roles
             and UserRole.ROLE_ADMIN in current_user.roles
         ):
             return False
         if (
             UserRole.ROLE_ADMIN in target_user.roles
             and UserRole.ROLE_ADMIN in current_user.roles
         ):
             return False
     return True

async def update_user(updated_user_params: dict, user_id: UUID, session) -> Union[UUID, None]:
    async with session.begin():
        user_dal = UserDAL(session)
        print(f"Updating user with params: {updated_user_params}") 
        result = await user_dal.update_user(
            user_id=user_id,
            **updated_user_params,
            updated_at=datetime.now()
        )
        return user_id