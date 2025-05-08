from datetime import timedelta
from typing import Union

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession

import core.config as settings
from schemas.users import Token
from db.dals.user_dal import UserDAL
from db.models.users import User
from db.session import get_db
from core.hashing import Hasher
from core.security import create_access_token

login_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")

async def get_user_by_email_for_auth(email: str, session):
    async with session.begin():
        user_dal = UserDAL(session)
        return await user_dal.get_user_by_email(
            email=email,
        )

async def authenticate_user(email: str, password: str, session) -> Union[User, None]:
    user = await get_user_by_email_for_auth(email=email, session=session)
    if not user:
        return None
    if not Hasher.verify_password(password, user.hashed_password):
        return None
    return user

@login_router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_db)
):
    user = await authenticate_user(form_data.username, form_data.password, session)
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

async def get_current_user_from_token(
    token: str = Depends(oauth2_scheme), 
    session: AsyncSession = Depends(get_db)
) -> User:
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
        
    user = await get_user_by_email_for_auth(email=email, session=session)
    if not user:
        raise credentials_exception
        
    return user

@login_router.get("/test_auth_endpoint")
async def sample_endpoint_under_jwt(
    current_user: User = Depends(get_current_user_from_token),
):
    return {"Success": True, "current_user": current_user}