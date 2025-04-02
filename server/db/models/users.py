import uuid
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, Integer, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID, ARRAY
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    DEFAULT_PHOTO = "/static/images/defaults/default-avatar.jpg"
    DEFAULT_HEADER_PHOTO = "/static/images/defaults/default-header.jpg"
    DEFAULT_FRAME_PHOTO = "/static/images/defaults/default-frame.png"

    user_id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    photo: Mapped[str] = mapped_column(String, nullable=False, default=DEFAULT_PHOTO)
    frame_photo: Mapped[str] = mapped_column(String, nullable=False, default=DEFAULT_FRAME_PHOTO)
    header_photo: Mapped[str] = mapped_column(String, nullable=False, default=DEFAULT_HEADER_PHOTO)

    name: Mapped[str] = mapped_column(String, nullable=False)
    surname: Mapped[str] = mapped_column(String, nullable=False)
    about: Mapped[str] = mapped_column(String, nullable=False, default="Пользователь ничего о себе не написал.")
    location: Mapped[str] = mapped_column(String, nullable=False, default="")
    age: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    # readed_manga: Mapped[list[UUID]] = mapped_column(ARRAY(UUID), nullable=False, default=[])
    # readed_chapters: Mapped[list[UUID]] = mapped_column(ARRAY(UUID), nullable=False, default=[])

    # comments: Mapped[list[UUID]] = mapped_column(ARRAY(UUID), nullable=False, default=[])
    # likes: Mapped[list[UUID]] = mapped_column(ARRAY(UUID), nullable=False, default=[])
    # dislikes: Mapped[list[UUID]] = mapped_column(ARRAY(UUID), nullable=False, default=[])
    # achievements: Mapped[list[UUID]] = mapped_column(ARRAY(UUID), nullable=False, default=[])

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

