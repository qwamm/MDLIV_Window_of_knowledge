from fastapi_controllers import Controller, get, post
from ..login_manager import login_manager
from src.database.models import User
from fastapi import Depends


class UserController(Controller):
    prefix = "/user"
    tags=["user"]

    def __init__(self):
        pass

    @get("/info")
    def info(self, user: User = Depends(login_manager)):
        # get user info
        pass
