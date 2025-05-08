import uuid
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, Integer, DateTime, Enum as SQLAlchemyEnum
from sqlalchemy.dialects.postgresql import ARRAY
from enum import Enum
from .base import Base

DEFAULT_PHOTO = "https://i.pinimg.com/736x/fd/02/55/fd02556bc6ce735541793834bd8725ce.jpg"
DEFAULT_HEADER_PHOTO = "https://i.pinimg.com/736x/9b/4d/ab/9b4dab17886caaab85a4a7eec70a3792.jpg"
DEFAULT_FRAME_PHOTO = "/static/images/defaults/default-frame.png"
DEFAULT_PROFILE_GRADIENT = "linear-gradient(to right, #000000, #000000)"

class UserRole(str, Enum):
    USER = "USER"
    MODERATOR = "MODERATOR"
    ADMIN = "ADMIN"
    SUPERADMIN = "SUPERADMIN"

    def can_moderate(self) -> bool:
        return self in [UserRole.MODERATOR, UserRole.ADMIN, UserRole.SUPERADMIN]

    def is_admin(self) -> bool:
        return self in [UserRole.ADMIN, UserRole.SUPERADMIN]

    def is_superadmin(self) -> bool:
        return self == UserRole.SUPERADMIN


class User(Base):
    __tablename__ = "users"

    role: Mapped[UserRole] = mapped_column(SQLAlchemyEnum(UserRole, name="user_role"), nullable=False, default=UserRole.USER)

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    
    username: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    photo: Mapped[str] = mapped_column(String, nullable=False, default=DEFAULT_PHOTO)
    frame_photo: Mapped[str] = mapped_column(String, nullable=True)
    header_photo: Mapped[str] = mapped_column(String, nullable=False, default=DEFAULT_HEADER_PHOTO)

    # profile_gradient: Mapped[str] = mapped_column(String, nullable=False, default=DEFAULT_PROFILE_GRADIENT)

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
        return self.role == role

    def can_moderate(self) -> bool:
        return self.role.can_moderate()

    def is_admin(self) -> bool:
        return self.role.is_admin()

    def is_superadmin(self) -> bool:
        return self.role.is_superadmin()

    def can_modify_user(self, target_user: 'User') -> bool:
        if self.user_id == target_user.user_id:
            return True

        if not self.is_active:
            return False

        if self.is_superadmin():
            return True

        if self.is_admin():
            return not (target_user.is_superadmin() or target_user.is_admin())

        if self.can_moderate():
            return not (target_user.is_superadmin() or target_user.is_admin() or target_user.can_moderate())

        return False

    def validate(self) -> bool:
        if not self.username or len(self.username) < 3:
            return False
        if not self.email or '@' not in self.email:
            return False
        if not self.name or not self.surname:
            return False
        if self.age < 0 or self.age > 150:
            return False
        return True