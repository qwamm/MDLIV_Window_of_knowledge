from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import joinedload
from sqlalchemy.future import select
from typing import List, Optional
from ..models import SearchLog


class SearchLogRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, search_log_id: int) -> Optional[SearchLog]:
        query = select(SearchLog).where(SearchLog.id == search_log_id).options(
            joinedload(SearchLog.user),
            joinedload(SearchLog.knowbase)
        )
        result = await self.session.execute(query)
        return result.scalars().first()

    async def delete_by_id(self, search_log_id: int) -> bool:
        query = delete(SearchLog).where(SearchLog.id == search_log_id)
        result = await self.session.execute(query)
        await self.session.commit()
        return result.rowcount > 0

    async def update_fields(
        self,
        search_log_id: int,
        query: Optional[str] = None,
        response_status: Optional[bool] = None
    ) -> Optional[SearchLog]:
        update_data = {}
        if query is not None:
            update_data["query"] = query
        if response_status is not None:
            update_data["responseStatus"] = response_status

        if not update_data:
            raise ValueError("Не переданы данные для обновления")

        query = (
            update(SearchLog)
            .where(SearchLog.id == search_log_id)
            .values(**update_data)
            .returning(SearchLog)
        )
        result = await self.session.execute(query)
        await self.session.commit()
        return result.scalars().first()

    async def get_all(self, limit: int = 100, offset: int = 0) -> List[SearchLog]:
        query = (
            select(SearchLog)
            .options(joinedload(SearchLog.user), joinedload(SearchLog.knowbase))
            .limit(limit)
            .offset(offset)
        )
        result = await self.session.execute(query)
        return result.scalars().all()