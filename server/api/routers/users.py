from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from schemas.users import UserCreate, UserRead, UserDeleteResponse, UserUpdateRequest, UserUpdateResponse
from db.session import get_db
from api.services.user_service import (
    create_new_user,
    delete_user,
    get_user,
    get_users,
    update_user
)

user_router = APIRouter()

@user_router.get("/", response_model=list[UserRead])
async def get_users_router(session: AsyncSession = Depends(get_db)) -> list[UserRead]:
    return await get_users(session)

@user_router.get("/{user_id}", response_model=UserRead)
async def get_user_router(user_id: UUID, session: AsyncSession = Depends(get_db)) -> UserRead:
    user = await get_user(user_id, session)
    if user is None:
        raise HTTPException(status_code=404, detail="User with id {user_id} not found")
    return user

@user_router.post("/", response_model=UserRead)
async def create_user_router(body: UserCreate, session: AsyncSession = Depends(get_db)) -> UserRead:
    return await create_new_user(body, session)

@user_router.patch("/{user_id}", response_model=UserUpdateResponse)
async def update_user_router(
        user_id: UUID, body: UserUpdateRequest, session: AsyncSession = Depends(get_db)
) -> UserUpdateResponse:
     updated_user_params = body.model_dump(exclude_none=True)
     if updated_user_params == {}:
         raise HTTPException(status_code=422, detail="At least one parameter for user update info should be provided")
     user = await get_user(user_id, session)
     if user is None:
         raise HTTPException(status_code=404, detail=f"User with id {user_id} not found.")
     updated_user_id = await update_user(updated_user_params=updated_user_params, user_id=user_id, session=session)
     return UserUpdateResponse(updated_user_id=user_id)

@user_router.delete("/{user_id}", response_model=UserDeleteResponse)
async def delete_user_router(user_id: UUID, session: AsyncSession = Depends(get_db)) -> UserDeleteResponse:
    deleted_user_id = await delete_user(user_id, session)
    if deleted_user_id is None:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    return UserDeleteResponse(user_id=deleted_user_id)

