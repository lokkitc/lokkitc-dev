from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.auth import get_current_user_from_token as get_current_user
from schemas.users import (
    UserCreate,
    UserRead,
    UserDeleteResponse,
    UserUpdateRequest,
    UserUpdateResponse,
    UserRoleUpdate,
    UserRoleUpdateResponse
)
from api.services.user_service import check_user_permissions
from db.session import get_db
from api.services.user_service import (
    create_new_user,
    delete_user,
    get_user,
    get_users,
    update_user,
    get_user_by_username,
    update_user_role,
)
from db.models.users import User

user_router = APIRouter()

@user_router.get("/", response_model=list[UserRead])
async def get_users_router(
    session: AsyncSession = Depends(get_db)
) -> list[UserRead]:
    return await get_users(session)

@user_router.get("/{user_id}", response_model=UserRead)
async def get_user_router(
    user_id: int,
    session: AsyncSession = Depends(get_db),
    current_user: UserRead = Depends(get_current_user)
) -> UserRead:
    user = await get_user(user_id, session)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail=f"User with id {user_id} not found"
        )
    return user

@user_router.post("/", response_model=UserRead)
async def create_user_router(
    body: UserCreate,
    session: AsyncSession = Depends(get_db)
) -> UserRead:
    return await create_new_user(body, session)

@user_router.patch("/{user_id}", response_model=UserRead)
async def update_user_router(
    user_id: int,
    body: UserUpdateRequest,
    session: AsyncSession = Depends(get_db),
    current_user: UserRead = Depends(get_current_user)
) -> UserRead:
    updated_user_params = body.model_dump(exclude_none=True)
    if not updated_user_params:
        raise HTTPException(
            status_code=422,
            detail="At least one parameter for user update info should be provided"
        )
    return await update_user(
        updated_user_params=updated_user_params,
        user_id=user_id,
        current_user=current_user,
        session=session
    )

@user_router.delete("/{user_id}", response_model=UserDeleteResponse)
async def delete_user_router(
    user_id: int,
    session: AsyncSession = Depends(get_db),
    current_user: UserRead = Depends(get_current_user)
) -> UserDeleteResponse:
    deleted_user_id = await delete_user(user_id, current_user, session)
    if deleted_user_id is None:
        raise HTTPException(
            status_code=404,
            detail=f"User with id {user_id} not found"
        )
    return UserDeleteResponse(user_id=deleted_user_id)

@user_router.get("/username/{username}", response_model=UserRead)
async def get_user_by_username_router(
    username: str,
    session: AsyncSession = Depends(get_db)
) -> UserRead:
    user = await get_user_by_username(username, session)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail=f"User with username {username} not found"
        )
    return user

@user_router.patch("/{user_id}/role", response_model=UserRoleUpdateResponse)
async def update_user_role_router(
    user_id: int,
    body: UserRoleUpdate,
    session: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> UserRoleUpdateResponse:
    return await update_user_role(user_id, body.role, current_user, session)

