from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import Record, Tag, File
from src.database import RecordRepository, TagRepository
from starlette.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST


class RecordService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.record_repository = RecordRepository(session)
        self.tag_repository = TagRepository(session)

    async def add_tag(self, tag_name: str, description: str, record_ids: list[int]) -> Tag:
        records = [await self.record_repository.get_by_id(record_id) for record_id in record_ids]
        if any(record is None for record in records):
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="One or more records not found")
        tag = await self.tag_repository.add_tag(tag_name, description, records)
        return tag

    async def delete_tag(self, tag_id: int) -> None:
        tag = await self.tag_repository.get_by_id(tag_id)
        if not tag:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Tag not found")
        await self.tag_repository.delete_file_by_id(tag_id)

    async def create_record(self, description: str, file_ids: list[int], tag_ids: list[int]) -> Record:
        files = [await self.record_repository.get_by_id(file_id) for file_id in file_ids]
        tags = [await self.tag_repository.get_by_id(tag_id) for tag_id in tag_ids]
        if any(file is None for file in files) or any(tag is None for tag in tags):
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="One or more files or tags not found")
        record = await self.record_repository.add_record(description, files, tags)
        return record

    async def delete_record(self, record_id: int) -> None:
        record = await self.record_repository.get_by_id(record_id)
        if not record:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Record not found")
        await self.record_repository.delete_file_by_id(record_id)
