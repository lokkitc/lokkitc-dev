from fastapi import HTTPException
from typing import Union
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from schemas.users import UserCreate, UserRead, UserUpdateRequest, UserRoleUpdateResponse
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
            role=UserRole.USER,
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
            updated_at=new_user.updated_at,
            role=new_user.role
        )

async def delete_user(user_id: int, current_user: User, session) -> Union[int, None]:
    async with session.begin():
        user_dal = UserDAL(session)
        target_user = await user_dal.get_user(user_id=user_id)
        
        if not target_user:
            raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
            
        if not current_user.can_modify_user(target_user):
            raise HTTPException(status_code=403, detail="You don't have permission to delete this user")
            
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
                updated_at=user.updated_at,
                role=user.role
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
                updated_at=user.updated_at,
                role=user.role
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
            updated_at=user.updated_at,
            role=user.role
            ) for user in users]

def check_user_permissions(target_user: User, current_user: User) -> bool:
    return current_user.can_modify_user(target_user)

async def update_user(updated_user_params: dict, user_id: int, current_user: User, session) -> UserRead:
    async with session.begin():
        user_dal = UserDAL(session)
        target_user = await user_dal.get_user(user_id=user_id)
        
        if not target_user:
            raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
            
        if not current_user.can_modify_user(target_user):
            raise HTTPException(status_code=403, detail="You don't have permission to modify this user")
            
        await user_dal.update_user(
            user_id=user_id,
            **updated_user_params,
            updated_at=datetime.now()
        )
        
        updated_user = await user_dal.get_user(user_id=user_id)
        
        return UserRead(
            user_id=updated_user.user_id,
            name=updated_user.name,
            surname=updated_user.surname,
            email=updated_user.email,
            is_active=updated_user.is_active,
            username=updated_user.username,
            photo=updated_user.photo,
            header_photo=updated_user.header_photo,
            frame_photo=updated_user.frame_photo,
            about=updated_user.about,
            location=updated_user.location,
            age=updated_user.age,
            created_at=updated_user.created_at,
            updated_at=updated_user.updated_at,
            role=updated_user.role
        )

async def update_user_role(user_id: int, role: UserRole, current_user: User, session) -> UserRoleUpdateResponse:
    async with session.begin():
        user_dal = UserDAL(session)
        target_user = await user_dal.get_user(user_id=user_id)
        
        if not target_user:
            raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
            
        if not current_user.is_superadmin():
            raise HTTPException(status_code=403, detail="Only superadmin can modify user roles")
            
        if target_user.is_superadmin() and not current_user.is_superadmin():
            raise HTTPException(status_code=403, detail="Cannot modify superadmin role")
            
        if role == UserRole.USER and target_user.is_superadmin():
            raise HTTPException(status_code=403, detail="Cannot downgrade superadmin to user")
            
        await user_dal.update_user(
            user_id=user_id,
            role=role,
            updated_at=datetime.now()
        )
        
        updated_user = await user_dal.get_user(user_id=user_id)
        
        return UserRoleUpdateResponse(
            user_id=updated_user.user_id,
            role=updated_user.role
        )

async def get_user_by_email(email: str, session: AsyncSession) -> User | None:
    async with session.begin():
        user_dal = UserDAL(session)
        return await user_dal.get_user_by_email(email)

async def get_user_by_id(user_id: int, session: AsyncSession) -> User | None:
    async with session.begin():
        user_dal = UserDAL(session)
        return await user_dal.get_user_by_id(user_id)

