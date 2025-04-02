from db.models.users import User
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import Union
from sqlalchemy import update, delete, select, and_

class UserDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(self, name: str, surname: str, username: str, email: str, hashed_password: str) -> User:
        new_user = User(
            name=name,
            surname=surname,
            username=username,
            email=email,
            hashed_password=hashed_password
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user
    
    async def delete_user(self, user_id: UUID) -> Union[User, None]:
        query = update(User).where(and_(
            User.user_id == user_id,
            User.is_active == True
        )).values(is_active=False).returning(User.user_id)
        result = await self.db_session.execute(query)
        deleted_user_by_id = result.fetchone()
        if deleted_user_by_id is not None:
            return deleted_user_by_id[0]
        return None
    
    async def get_user(self, user_id: UUID) -> Union[User, None]:
        query = select(User).where(User.user_id == user_id)
        result = await self.db_session.execute(query)
        user_by_id = result.fetchone()
        if user_by_id is not None:
            return user_by_id[0]
        return None
    
    async def get_user_by_username(self, username: str) -> Union[User, None]:
        query = select(User).where(User.username == username)
        result = await self.db_session.execute(query)
        user_by_username = result.fetchone()
        if user_by_username is not None:
            return user_by_username[0]
        return None
    
    async def get_users(self) -> list[User]:
        query = select(User).where(User.is_active == True)
        result = await self.db_session.execute(query)
        users = result.fetchall()
        return [user[0] for user in users]

    async def update_user(self, user_id: UUID, **kwargs) -> Union[UUID, None]:
        query = update(User).\
            where(and_(User.user_id == user_id, User.is_active == True)).\
            values(kwargs).\
            returning(User.user_id)
        res = await self.db_session.execute(query)
        update_user_id_row = res.fetchone()
        if update_user_id_row is not None:
            return update_user_id_row[0]
        return None
    

    async def get_user_by_email(self, email: str) -> Union[User, None]:
        query = select(User).where(User.email == email)
        res = await self.db_session.execute(query)
        user_row = res.fetchone()
        if user_row is not None:
            return user_row[0]
        return None
