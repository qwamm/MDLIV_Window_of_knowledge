import secrets
from typing import Optional

from sqlalchemy import select
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.ext.asyncio import AsyncSession
from werkzeug.security import check_password_hash, generate_password_hash

from .. import UsersBase
from ..models import User, KnowBase


class KnowBaseRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_id(self, id: int) -> UsersBase | None:
        stmt = select(UsersBase).where(UsersBase.id == id).limit(1)
        return await self.session.scalar(stmt)

    async def get_by_name(self, base_name: str) -> KnowBase | None:
        stmt = select(KnowBase).where(KnowBase.name == base_name).limit(1)
        return await self.session.scalar(stmt)

    async def get_users_by_KnowBase(self, knowbase: KnowBase) -> list[User] | None:
        return knowbase.users

    async def add_user_to_UsersBase(self, usersbase: UsersBase, user: User, roles: list[int]) -> None:
        stmt = insert(UsersBase).values(user=user, roles=roles)
        await self.session.flush()