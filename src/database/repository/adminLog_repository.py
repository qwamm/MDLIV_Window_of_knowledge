from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy import delete
from typing import Optional
from datetime import datetime
from ..models import AdminLog  # Замените на ваш путь к модели AdminLog


class AdminLogRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, log_id: int) -> Optional[AdminLog]:
        query = select(AdminLog).where(AdminLog.id == log_id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_all(self, limit: int = 100, offset: int = 0) -> list[AdminLog]:
        query = select(AdminLog).limit(limit).offset(offset)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def delete_by_id(self, log_id: int) -> bool:
        query = delete(AdminLog).where(AdminLog.id == log_id)
        result = await self.session.execute(query)
        if result.rowcount > 0:
            await self.session.commit()
            return True
        return False

    async def create_log(self, user_id: int, knowbase_id: Optional[int], action: str) -> AdminLog:
        log = AdminLog(
            user_id=user_id,
            knowbase_id=knowbase_id,
            action=action,
            timestamp=datetime.utcnow(),
        )
        self.session.add(log)
        await self.session.commit()
        await self.session.refresh(log)
        return log