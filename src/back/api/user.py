from fastapi_controllers import Controller, get, post
from ..login_manager import login_manager
from src.database.models import User
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.domain import UserService
from src.database import get_db_session


class UserController(Controller):
    prefix = "/user"
    tags=["user"]

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session
        self.user_service = UserService(session)

    @get("/info")
    async def info(self, user: User = Depends(login_manager)):
        profile = await self.user_service.get_by_id(user.id)
        return {'id': profile.id,
                'user_name': profile.username,
                'first_name': profile.first_name,
                'second_name': profile.second_name}
