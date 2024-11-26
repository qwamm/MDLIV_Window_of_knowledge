from fastapi_controllers import Controller, get, post
from pydantic import BaseModel
from fastapi import Depends
from ..login_manager import login_manager


class LoginRequest(BaseModel):
    user_name: str
    password: str
    remember_me: bool


class RegisterRequest(BaseModel):
    user_name: str
    password: str
    password_again: str

class AuthController(Controller):
    prefix="/auth"

    def __init__(self):
        pass

    @post("/login")
    def login(self, request: LoginRequest):
        # compare user with db
        return {"message": "OK"}

    @post("/register")
    def register(self, request: RegisterRequest):
        # throw user to db
        return {"message": "OK"}

    @post("/logout")
    def logout(self):
        # logout
        return {"message": "OK"}
