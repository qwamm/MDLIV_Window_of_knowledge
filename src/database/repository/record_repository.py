import secrets
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.util import await_only
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import delete

from ..models import File, Record, Tag
from ..models.models import record_files_table, knowbase_users_table


class RecordRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_id(self, id: int) -> File | None:
        stmt = select(Record).where(Record.id == id).limit(1)
        return await self.session.scalar(stmt)

    def get_records(self, file: File) -> list[Record] | None:
        return file.records

    async def add_record(self, decription: str, files: list[File], tags: list[Tag]) -> Record | None:
        record = Record(description=decription)
        self.session.add(record)
        await self.add_file_to_record(files)
        await self.add_tag_to_record(tags)
        return await self.get_by_id(record.id)

    async def add_file_to_record(self, files: list[File]) -> None:
        Record.files += files
        await self.session.flush()

    async def add_tag_to_record(self, tags: list[Tag]) -> None:
        Record.tags += tags
        await self.session.flush()

    async def delete_file_by_id(self, id: int, files: File) -> None:
        stmt = delete(Record).where(Record.id == id)
        await self.session.execute(stmt)
        await self.session.commit()