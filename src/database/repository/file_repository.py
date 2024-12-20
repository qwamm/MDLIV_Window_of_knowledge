import secrets
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.util import await_only
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import delete

from ..models import File, Record
from ..models.models import record_files_table, knowbase_users_table


class FileRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_id(self, id: int) -> File | None:
        stmt = select(File).where(File.id == id).limit(1)
        return await self.session.scalar(stmt)

    def get_records(self, file: File) -> list[Record] | None:
        return file.records

    async def add_file(self, type: str, URL: str, keywords: list[str], record: Record) -> File | None:
        file = File(type=type, URL=URL, keywords=keywords)
        self.session.add(file)
        await self.add_record_to_file(file, [record])
        return await self.get_by_id(file.id)

    async def add_record_to_file(self, file: File, records: list[Record]) -> None:
        file.records += records
        await self.session.flush()

    async def delete_file_by_id(self, id: int, files: File) -> None:
        stmt = delete(File).where(File.id == id)
        await self.session.execute(stmt)
        await self.session.commit()





