from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import File, Record
from src.database import FileRepository
from starlette.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST


class FileService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.file_repository = FileRepository(session)

    async def get_file_url(self, file_id: int) -> str:
        file = await self.file_repository.get_by_id(file_id)
        if not file:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="File not found")
        return file.URL

    async def set_keywords(self, file_id: int, keywords: list[str]) -> None:
        file = await self.file_repository.get_by_id(file_id)
        if not file:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="File not found")
        file.keywords = keywords
        await self.session.commit()

    async def add_file(self, file_type: str, url: str, keywords: list[str], record: Record) -> File:
        file = await self.file_repository.add_file(file_type, url, keywords, record)
        if not file:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Failed to add file")
        return file

    async def delete_file(self, file_id: int) -> None:
        file = await self.file_repository.get_by_id(file_id)
        if not file:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="File not found")
        await self.file_repository.delete_file_by_id(file_id)