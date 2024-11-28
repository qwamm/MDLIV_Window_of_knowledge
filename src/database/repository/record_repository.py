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

    async def get_by_id(self, id: int) -> Record | None:
        stmt = select(Record).where(Record.id == id).limit(1)
        return await self.session.scalar(stmt)

    def get_records(self, file: File) -> list[Record] | None:
        return file.records

    async def add_record(self, decription: str, files: list[File], tags: list[Tag], knowbase_id: int) -> Record | None:
        record = Record(description=decription, knowbase_id=knowbase_id)
        self.session.add(record)
        await self.session.commit()
        await self.add_file_to_record(files)
        await self.add_tag_to_record(tags)
        return await self.get_by_id(record.id)

    async def add_file_to_record(self, files: list[File]) -> None:
        #record = await self.get_by_id(id)
        for file in files:
            Record.files.append(file)
        await self.session.flush()

    async def add_tag_to_record(self, tags: list[Tag]) -> None:
        #record = await self.get_by_id(id)
        for tag in tags:
            Record.tags.append(tag)
        await self.session.flush()

    async def delete_record_by_id(self, id: int) -> None:
        record = await self.get_by_id(id)
        await self.session.delete(record)
        await self.session.commit()
        return record

