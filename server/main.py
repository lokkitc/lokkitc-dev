from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import settings
from sqlalchemy.dialects.postgresql import UUID
import uuid
import re
from fastapi import HTTPException
from typing import BaseModel, EmailStr, validator
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean

engine = create_async_engine(settings.REAL_DATABASE_URL, echo=True, future=True)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    email: Mapped[EmailStr] = mapped_column(EmailStr, unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
