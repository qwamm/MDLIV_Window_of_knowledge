from fastapi import HTTPException
from src.database import User, KnowBase
from src.database import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_login.exceptions import InvalidCredentialsException
from starlette.status import HTTP_400_BAD_REQUEST


class UserService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.profile_repository = UserRepository(session)

    async def get_by_id(self, id: int) -> User:
        return await self.profile_repository.get_by_id(id)

    async def login(self, login: str, password: str) -> User:
        profile = await self.profile_repository.get_by_auth(login, password)
        if profile is None:
            raise InvalidCredentialsException
        return profile

    async def registration(self, login: str, password: str, repeat_password: str):
        if password != repeat_password:
            raise HTTPException(HTTP_400_BAD_REQUEST, "Passwords don't match")
        if await self.profile_repository.get_by_username(login) is not None:
            raise HTTPException(HTTP_400_BAD_REQUEST, "User already exist")
        await self.profile_repository.registration(login, password)

    async def get_knowbases_by_id(self, id: int) -> list[KnowBase]:
        know_bases = await self.profile_repository.get_knowbases_by_id(id)
        if know_bases is None:
            return list()
        return know_bases
