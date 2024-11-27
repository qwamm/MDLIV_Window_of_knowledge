from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import Customization


class CustomizationRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_id(self, id: int) -> Customization | None:
        stmt = select(Customization).where(Customization.id == id).limit(1)
        return await self.session.scalar(stmt)

    async def delete_customization(self, id: int) -> None:
        stmt = delete(Customization).where(Customization.id == id)
        await self.session.execute(stmt)
        await self.session.commit()

    async def set_font(self, id: int, font: str) -> None:
        stmt = update(Customization).where(Customization.id == id).values(font=font)
        await self.session.execute(stmt)
        await self.session.commit()

    async def update_font(self, id: int, new_font: str) -> None:
        await self.set_font(id, new_font)

    async def remove_logo(self, id: int) -> None:
        stmt = update(Customization).where(Customization.id == id).values(logo_URL=None)
        await self.session.execute(stmt)
        await self.session.commit()

    async def add_logo(self, id: int, logo_URL: str) -> None:
        stmt = update(Customization).where(Customization.id == id).values(logo_URL=logo_URL)
        await self.session.execute(stmt)
        await self.session.commit()

    async def change_knowbase_id(self, id: int, new_knowbase_id: int) -> None:
        stmt = update(Customization).where(Customization.id == id).values(knowbase_id=new_knowbase_id)
        await self.session.execute(stmt)
        await self.session.commit()
