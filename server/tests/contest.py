from typing import Generator, Any
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import pytest
import settings
from starlette.testclient import TestClient
import os
import asyncio
from db.session import get_db
import asyncpg
from server.main import app

test_engine = create_async_engine(settings.DATABASE_URL.replace("postgresql", "postgresql+asyncpg"))
