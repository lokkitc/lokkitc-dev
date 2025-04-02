import re
import uuid
from fastapi import HTTPException
from pydantic import BaseModel, field_validator, EmailStr, constr
from typing import Optional
from datetime import datetime
LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-\s]+$")



class TunedModel(BaseModel):
    class Config:
        from_attributes = True


class UserRead(TunedModel):
    user_id: uuid.UUID
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

class UserCreate(BaseModel):
    name: str
    surname: str
    username: str
    email: EmailStr
    password: str

    @field_validator("name", "surname", mode="before")
    def validate_name(cls, v):
        if not LETTER_MATCH_PATTERN.match(v):
            raise HTTPException(
                status_code=422,
                detail="Must contain only letters"
            )
        return v

class UserUpdateRequest(BaseModel):
    name: Optional[constr(min_length=1, max_length=100)] = None    
    surname: Optional[constr(min_length=1, max_length=100)] = None
    username: Optional[constr(min_length=1, max_length=100)] = None
    photo: Optional[constr(min_length=1, max_length=1000)] = None
    header_photo: Optional[constr(min_length=1, max_length=1000)] = None
    email: Optional[EmailStr] = None
    about: Optional[constr(min_length=1, max_length=1000)] = None
    location: Optional[constr(min_length=1, max_length=100)] = None
    age: Optional[int] = None
    frame_photo: Optional[constr(min_length=1, max_length=1000)] = None


    class Config:
        extra = "forbid"
        validate_assignment = True

class UserDeleteResponse(BaseModel):
    user_id: uuid.UUID

class UserUpdateResponse(BaseModel):
    updated_user_id: uuid.UUID

class Token(BaseModel):
    access_token: str
    token_type: str

