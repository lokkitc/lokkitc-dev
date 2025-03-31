from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.users import UserCreate, UserRead, UserDeleteResponse, UserUpdateRequest, UserUpdateResponse
from db.dals import UserDAL
from db.session import get_db

from fastapi import HTTPException
from uuid import UUID
from typing import Union
from core.hashing import Hasher

user_router = APIRouter()
async def _create_new_user(body: UserCreate, db) -> UserRead:
    async with db as session:
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
        
async def _delete_user(user_id, db) -> Union[UUID, None]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            deleted_user_id = await user_dal.delete_user(
                user_id=user_id
            )
            return deleted_user_id



async def _get_user(user_id, db) -> Union[UserRead, None]:
    async with db as session:
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
        
async def _get_users(db) -> list[UserRead]:
    async with db as session:
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


async def _update_user(updated_user_params: dict, user_id: UUID, db) -> Union[UUID, None]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            print(f"Updating user with params: {updated_user_params}") 
            result = await user_dal.update_user(
                user_id=user_id,
                **updated_user_params
            )
            await session.commit() 
            return user_id

@user_router.get("/", response_model=list[UserRead])
async def get_users(db: AsyncSession = Depends(get_db)) -> list[UserRead]:
    return await _get_users(db)

@user_router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: UUID, db: AsyncSession = Depends(get_db)) -> UserRead:
    user = await _get_user(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User with id {user_id} not found")
    return user

@user_router.post("/", response_model=UserRead)
async def create_user(body: UserCreate, db: AsyncSession = Depends(get_db)) -> UserRead:
    return await _create_new_user(body, db)

@user_router.patch("/{user_id}", response_model=UserUpdateResponse)
async def update_user(
        user_id: UUID, body: UserUpdateRequest, db: AsyncSession = Depends(get_db)
) -> UserUpdateResponse:
     updated_user_params = body.model_dump(exclude_none=True)
     if updated_user_params == {}:
         raise HTTPException(status_code=422, detail="At least one parameter for user update info should be provided")
     user = await _get_user(user_id, db)
     if user is None:
         raise HTTPException(status_code=404, detail=f"User with id {user_id} not found.")
     updated_user_id = await _update_user(updated_user_params=updated_user_params, user_id=user_id, db=db)
     return UserUpdateResponse(updated_user_id=user_id)

@user_router.delete("/{user_id}", response_model=UserDeleteResponse)
async def delete_user(user_id: UUID, db: AsyncSession = Depends(get_db)) -> UserDeleteResponse:
    deleted_user_id = await _delete_user(user_id, db)
    if deleted_user_id is None:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    return UserDeleteResponse(user_id=deleted_user_id)

