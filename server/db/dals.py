from db.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import Union
from sqlalchemy import update, delete, select, and_

class UserDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(self, name: str, surname: str, email: str) -> User:
        new_user = User(
            name=name,
            surname=surname,
            email=email
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user
    
    async def delete_user(self, user_id: UUID) -> Union[User, None]:
        query = update(User).where(and_(User.user_id == user_id, User.is_active == True)).values(is_active=False).returning(User.user_id)
        result = await self.db_session.execute(query)
        deleted_user_by_id = result.fetchone()
        if deleted_user_by_id is not None:
            return deleted_user_by_id[0]
        return None
    
    async def get_user(self, user_id: UUID) -> Union[User, None]:
        query = select(User).where(User.user_id == user_id)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()