import secrets
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from werkzeug.security import check_password_hash, generate_password_hash

from ..models import User, KnowBase, Record


class KnowBaseRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_id(self, id: int) -> KnowBase | None:
        stmt = select(KnowBase).where(KnowBase.id == id).limit(1)
        return await self.session.scalar(stmt)

    async def get_by_name(self, base_name: str) -> KnowBase | None:
        stmt = select(KnowBase).where(KnowBase.name == base_name).limit(1)
        return await self.session.scalar(stmt)

    async def get_users_by_KnowBase(self, knowbase: KnowBase) -> list[User] | None:
        return knowbase.users

    async def add_user_to_KnowBase(self, id: int, user: User) -> KnowBase | None:
        know_base = await self.get_by_id(id)
        if know_base is not None:
            know_base.users.append(user)
            await self.session.flush()
        return know_base

    async def create_KnowBase(self, name: str, description: str) -> None:
        know_base = KnowBase(name=name, description=description)
        self.session.add(know_base)
        await self.session.commit()

    async def delete_KnowBase(self, id: int) -> KnowBase | None:
        know_base = await self.get_by_id(id)
        await self.session.delete(know_base)
        await self.session.commit()
        return know_base

    async def add_record(self, id: int, record: Record) -> KnowBase | None:
        know_base = await self.get_by_id(id)
        if know_base is not None:
            know_base.records.append(record.id)
            await self.session.commit()
        return know_base

    async def delete_record(self, id: int, record: Record) -> KnowBase | None:
        know_base = await self.get_by_id(id)
        if know_base is not None:
            know_base.records.remove(record.id)
            await self.session.commit()
        return know_base
