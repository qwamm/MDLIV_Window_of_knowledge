from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import File, Record
from src.database import KnowBaseRepository
from starlette.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from src.database import User, KnowBase


class KnowBaseService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.knowbase_repository = KnowBaseRepository(session)

    async def get_by_id(self, id: int) -> KnowBase:
        knowbase = await self.knowbase_repository.get_by_id(id)
        if knowbase is None:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Knowbase not found")
        return knowbase

    async def get_by_name(self, base_name: str) -> KnowBase:
        knowbase = await self.knowbase_repository.get_by_name(base_name)
        if knowbase is None:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Knowbase not found")
        return knowbase

    async def get_users_by_KnowBase(self, knowbase: KnowBase) -> list[User] | None:
        return await self.knowbase_repository.get_users_by_KnowBase(knowbase)

    async def add_user_to_KnowBase(self, id: int, user: User) -> KnowBase:
        knowbase = await self.knowbase_repository.add_user_to_KnowBase(id, user)
        if knowbase is None:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Knowbase not found")
        return knowbase

    async def create_KnowBase(self, name: str, description: str) -> None:
        await self.knowbase_repository.create_KnowBase(name, description)

    async def delete_KnowBase(self, id: int) -> KnowBase:
        knowbase = await self.knowbase_repository.delete_KnowBase(id)
        if knowbase is None:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Knowbase not found")
        return knowbase

    async def add_record(self, id: int, record: Record) -> KnowBase:
        knowbase = await self.knowbase_repository.add_record(id, record)
        if knowbase is None:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Knowbase not found")
        return knowbase

    async def delete_record(self, id: int, record: Record) -> KnowBase:
        knowbase = await self.knowbase_repository.delete_record(id, record)
        if knowbase is None:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Knowbase not found")
        return knowbase
