import re
import uuid
from fastapi import HTTPException
from pydantic import BaseModel, field_validator, EmailStr, constr
from typing import Optional, List
from datetime import datetime
from db.models.users import UserRole
LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-\s]+$")



class TunedModel(BaseModel):
    class Config:
        from_attributes = True


class UserRead(TunedModel):
    user_id: int
    name: str
    surname: str
    username: str
    photo: str
    header_photo: str
    email: EmailStr
    about: str
    location: str
    age: int
    created_at: datetime
    updated_at: datetime
    is_active: bool
    frame_photo: Optional[str] = None

class UserBase(BaseModel):
    name: str
    surname: str
    username: str
    email: EmailStr

    @field_validator("name", "surname", mode="before")
    def validate_name(cls, v):
        if not LETTER_MATCH_PATTERN.match(v):
            raise ValueError("Must contain only letters")
        return v


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class UserInDB(UserBase):
    user_id: int
    is_active: bool = True
    created_at: datetime
    updated_at: datetime
    photo: str
    header_photo: str
    frame_photo: Optional[str] = None
    about: str
    location: str
    age: int

    class Config:
        from_attributes = True


class User(UserInDB):
    pass

class UserUpdateRequest(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    photo: Optional[str] = None
    header_photo: Optional[str] = None
    frame_photo: Optional[str] = None
    about: Optional[str] = None
    location: Optional[str] = None
    age: Optional[int] = None


    class Config:
        extra = "forbid"
        validate_assignment = True

class UserDeleteResponse(BaseModel):
    user_id: int

class UserUpdateResponse(BaseModel):
    updated_user_id: int

class Token(BaseModel):
    access_token: str
    token_type: str

class UserRoleUpdate(BaseModel):
    role: UserRole

class UserRoleUpdateResponse(BaseModel):
    user_id: int
    role: UserRole

