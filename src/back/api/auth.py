import json

from fastapi_controllers import Controller, get, post
from pydantic import BaseModel
from fastapi import Depends, Response
from ..login_manager import login_manager
from src.domain import UserService
from src.database import User
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_db_session
from datetime import timedelta


class LoginRequest(BaseModel):
    user_name: str
    password: str


class RegisterRequest(BaseModel):
    user_name: str
    first_name: str | None
    second_name: str | None
    password: str
    password_again: str


class AuthController(Controller):
    prefix="/auth"
    tags=["auth"]

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session
        self.user_service = UserService(session)

    @post("/login")
    async def login(self, response: Response, request: LoginRequest):
        user = await self.user_service.login(request.user_name, request.password)
        user_json = {
                "ID": user.id,
                "Secret": user.secret
            }
        access_token = login_manager.create_access_token(
            data={"sub" : json.dumps(user_json)},
            expires=timedelta(
                days=30)
        )
        response.set_cookie("access-token", access_token, max_age=60*60*24, httponly=True)

        return {"message": "OK"}

    @post("/register")
    async def register(self, request: RegisterRequest):
        await self.user_service.registration(request.user_name, request.first_name, request.second_name,
                                             request.password, request.password_again)
        await self.session.commit()
        return {"message": "OK"}

    @post("/logout")
    async def logout(self, response: Response, user: User = Depends(login_manager)):
        response.set_cookie("access-token", "", 0, httponly=True)
        return {"message": "OK"}
