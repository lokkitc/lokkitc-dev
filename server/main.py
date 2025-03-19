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




