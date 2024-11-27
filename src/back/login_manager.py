from fastapi_login import LoginManager
from ..enviroments import SECRET_KEY
from src.database import sessionmanager, UserRepository
import json

login_manager = LoginManager(SECRET_KEY, "/api/auth/login", use_cookie=True)

@login_manager.user_loader()
async def load_user(userStr: str):
    async with sessionmanager.session() as session:
        profileRepository = UserRepository(session)
        user: dict = json.loads(userStr)
        id: int | None = user.get("ID", None)
        secret = user.get("Secret", None)
        if id is None or user is None:
            return None
        profile = await profileRepository.get_by_id(id)
        if profile is None:
            return None
        if profile.secret == secret:
            return profile
        return None
