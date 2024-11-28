from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete, and_
from src.database import SearchLog


class LogService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def delete_log_by_id(self, log_id: int) -> bool:
        stmt = delete(SearchLog).where(SearchLog.id == log_id)
        result = await self.session.execute(stmt)
        if result.rowcount > 0:
            await self.session.commit()
            return True
        return False

    async def get_logs_by_period(self, start_date: datetime, end_date: datetime) -> list[SearchLog]:
        stmt = select(SearchLog).where(
            and_(
                SearchLog.timestamp >= start_date,
                SearchLog.timestamp <= end_date
            )
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def find_similar_queries(self, query: str) -> list[SearchLog]:
        stmt = select(SearchLog).where(SearchLog.query.ilike(f"%{query}%"))
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_logs_by_user_id(self, user_id: int) -> list[SearchLog]:
        stmt = select(SearchLog).where(SearchLog.user_id == user_id)
        result = await self.session.execute(stmt)
        return result.scalars().all()