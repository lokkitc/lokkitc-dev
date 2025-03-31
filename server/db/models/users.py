import uuid

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    DEFAULT_PHOTO = "https://ui-avatars.com/api/?background=random&size=150&rounded=true&format=png"
    
    user_id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(String, nullable=False)
    photo: Mapped[str] = mapped_column(String, nullable=False, default=DEFAULT_PHOTO)
    name: Mapped[str] = mapped_column(String, nullable=False)
    surname: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
