from datetime import timedelta
from typing import Union

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession

import core.config as settings
from schemas.users import Token
from db.dals import UserDAL
from db.models.users import User
from db.session import get_db
from core.hashing import Hasher
from core.security import create_access_token

login_router = APIRouter()


async def _get_user_by_email_for_auth(email: str, db: AsyncSession):
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            return await user_dal.get_user_by_email(
                email=email,
            )


async def authenticate_user(email: str, password: str, db: AsyncSession) -> Union[User, None]:
    """Аутентифицирует пользователя по email и паролю.

    Args:
        email: Email пользователя
        password: Пароль пользователя
        db: Сессия базы данных

    Returns:
        User если аутентификация успешна, None в противном случае
    """
    user = await _get_user_by_email_for_auth(email=email, db=db)
    if not user:
        return None
    if not Hasher.verify_password(password, user.hashed_password):
        return None
    return user


@login_router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)
):
    user = await authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email, "other_custom_data": [1, 2, 3, 4]},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")


async def get_current_user_from_token(
    token: str = Depends(oauth2_scheme), 
    db: AsyncSession = Depends(get_db)
) -> User:
    """Получает текущего пользователя из JWT токена.

    Args:
        token: JWT токен
        db: Сессия базы данных

    Returns:
        User объект текущего пользователя

    Raises:
        HTTPException: если токен недействителен
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    
    try:
        payload = jwt.decode(
            token, 
            settings.SECRET_KEY, 
            algorithms=[settings.ALGORITHM]
        )
        email: str = payload.get("sub")
        
        if not email:
            raise credentials_exception
            
    except JWTError:
        raise credentials_exception
        
    user = await _get_user_by_email_for_auth(email=email, db=db)
    if not user:
        raise credentials_exception
        
    return user


@login_router.get("/test_auth_endpoint")
async def sample_endpoint_under_jwt(
    current_user: User = Depends(get_current_user_from_token),
):
    return {"Success": True, "current_user": current_user}