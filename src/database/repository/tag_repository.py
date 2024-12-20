import secrets
from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.util import await_only
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import delete

from .. import Record
from ..models import File, Record, Tag
from ..models.models import record_files_table, knowbase_users_table


class TagRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_id(self, id: int) -> Tag | None:
        stmt = select(Tag).where(Tag.id == id).limit(1)
        return await self.session.scalar(stmt)

    def get_records(self, tag: Tag) -> list[Record]:
        return tag.records

    async def add_tag(self, tag_name: str, description: str, records: list[Record]) -> Tag | None:
        tag = Tag(description=description, tag_name=tag_name)
        self.session.add(tag)
        await self.add_record_to_tag(tag.id, records)
        await self.session.commit()
        return await self.get_by_id(tag.id)

    async def add_record_to_tag(self, id: int, records: list[Record]) -> Tag | None:
        tag = await self.get_by_id(id)
        if tag is not None:
            for record in records:
                tag.records.append(record)
        await self.session.flush()
        return tag

    async def delete_tag_by_id(self, id: int) -> None:
        stmt = delete(Tag).where(Tag.id == id)
        await self.session.execute(stmt)
        await self.session.commit()
