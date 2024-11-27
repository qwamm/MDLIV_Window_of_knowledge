import secrets
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from werkzeug.security import check_password_hash, generate_password_hash

from ..models import User, KnowBase


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_id(self, id: int) -> User | None:
        stmt = select(User).where(User.id == id).limit(1)
        return await self.session.scalar(stmt)

    async def get_by_username(self, username: str) -> User | None:
        stmt = select(User).where(User.username == username).limit(1)
        return await self.session.scalar(stmt)

    async def get_by_auth(self, username: str, password: str) -> User | None:
        profile = await self.get_by_username(username)
        if profile is None:
            return None
        if not self.compare_password(profile, password):
            return None
        return profile

    async def registration(self, username: str, password: str, first_name: str, second_name:str = None) -> User | None:
        profile = User(username=username, first_name=first_name, second_name=second_name)
        self.session.add(profile)
        await self.set_password(profile, password)
        return await self.get_by_id(profile.id)

    async def set_password(self, profile: User, new_password: str) -> None:
        profile.password = generate_password_hash(new_password)
        profile.secret = secrets.token_urlsafe(8)
        await self.session.flush()

    def compare_password(self, profile: User, password: str) -> bool:
        old_password = profile.password
        if old_password is None:
            old_password = ""
        return check_password_hash(old_password, password)

    async def get_knowbases_by_id(self, id: int) -> list[KnowBase] | None:
        stmt = await self.get_by_id(id)
        if stmt is not None:
            return stmt.knowbases
        return None



