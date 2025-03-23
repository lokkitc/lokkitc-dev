import re
import uuid
from fastapi import HTTPException
from pydantic import BaseModel, field_validator, EmailStr

LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z]+$")



class TunedModel(BaseModel):
    class Config:
        from_attributes = True


class UserRead(TunedModel):
    user_id: uuid.UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool

class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr

    @field_validator("name", "surname", mode="before")
    def validate_name(cls, v):
        if not LETTER_MATCH_PATTERN.match(v):
            raise HTTPException(
                status_code=422,
                detail="Must contain only letters"
            )
        return v

class UserDeleteResponse(BaseModel):
    user_id: uuid.UUID

class UpdateUserResponse(BaseModel):
    updated_user_id: uuid.UUID
