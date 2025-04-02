import uuid
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, Integer, DateTime, Enum as SQLAlchemyEnum
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from enum import Enum



Base = declarative_base()

DEFAULT_PHOTO = "/static/images/defaults/default-avatar.jpg"
DEFAULT_HEADER_PHOTO = "/static/images/defaults/default-header.jpg"
DEFAULT_FRAME_PHOTO = "/static/images/defaults/default-frame.png"

class UserRole(str, Enum):
    ROLE_USER = "ROLE_USER"
    ROLE_MODERATOR = "ROLE_MODERATOR"
    ROLE_ADMIN = "ROLE_ADMIN"
    ROLE_SUPERADMIN = "ROLE_SUPERADMIN"

    def can_moderate(self) -> bool:
        return self in [UserRole.ROLE_MODERATOR, UserRole.ROLE_ADMIN, UserRole.ROLE_SUPERADMIN]

    def is_admin(self) -> bool:
        return self in [UserRole.ROLE_ADMIN, UserRole.ROLE_SUPERADMIN]

    def is_superadmin(self) -> bool:
        return self == UserRole.ROLE_SUPERADMIN


class User(Base):
    __tablename__ = "users"

    roles: Mapped[list[UserRole]] = mapped_column(ARRAY(SQLAlchemyEnum(UserRole, name="user_role")), nullable=False, default=[UserRole.ROLE_USER])

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

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    # readed_manga: Mapped[list[UUID]] = mapped_column(ARRAY(UUID), nullable=False, default=[])
    # readed_chapters: Mapped[list[UUID]] = mapped_column(ARRAY(UUID), nullable=False, default=[])

    # comments: Mapped[list[UUID]] = mapped_column(ARRAY(UUID), nullable=False, default=[])
    # likes: Mapped[list[UUID]] = mapped_column(ARRAY(UUID), nullable=False, default=[])
    # dislikes: Mapped[list[UUID]] = mapped_column(ARRAY(UUID), nullable=False, default=[])
    # achievements: Mapped[list[UUID]] = mapped_column(ARRAY(UUID), nullable=False, default=[])

    def has_role(self, role: UserRole) -> bool:
        return role in self.roles

    def can_moderate(self) -> bool:
        return any(role.can_moderate() for role in self.roles)

    def is_admin(self) -> bool:
        return any(role.is_admin() for role in self.roles)

    def is_superadmin(self) -> bool:
        return any(role.is_superadmin() for role in self.roles)