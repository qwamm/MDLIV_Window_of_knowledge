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

class MessageRequest(BaseModel):
    user_request: str
    kb_id: int

class ChatController(Controller):
    prefix = "/chat"
    tags=["chat"]

    def __init__(self):
        pass

    @post("/message")
    def message(self, request: MessageRequest):
        pass