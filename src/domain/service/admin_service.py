from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import AccessPolicy, User, KnowBase, Customization
from src.database import UserRepository, KnowBaseRepository
from starlette.status import HTTP_404_NOT_FOUND


class AdminService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.user_repository = UserRepository(session)
        self.knowbase_repository = KnowBaseRepository(session)

    async def set_access_policy(self, user_id: int, ip_addresses: list[str], policy: bool) -> AccessPolicy:
        user = await self.user_repository.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
        access_policy = AccessPolicy(user_id=user_id, ip_addresses=ip_addresses, policy=policy)
        self.session.add(access_policy)
        await self.session.commit()
        return access_policy

    async def add_user_to_knowbase(self, knowbase_id: int, user_id: int) -> None:
        knowbase = await self.knowbase_repository.get_by_id(knowbase_id)
        user = await self.user_repository.get_by_id(user_id)
        if not knowbase:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Knowledge base not found")
        if not user:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
        knowbase.users.append(user)
        await self.session.commit()

    async def save_customization(self, knowbase_id: int, font: str, logo_url: str) -> Customization:
        knowbase = await self.knowbase_repository.get_by_id(knowbase_id)
        if not knowbase:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Knowledge base not found")
        customization = knowbase.customization
        if not customization:
            customization = Customization(knowbase_id=knowbase_id, font=font, logo_URL=logo_url)
            self.session.add(customization)
        else:
            customization.font = font
            customization.logo_URL = logo_url
        await self.session.commit()
        return customization
