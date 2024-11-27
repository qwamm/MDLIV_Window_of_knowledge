from fastapi import APIRouter
from .auth import AuthController
from .user import UserController
from .chat import ChatController
from .knowledge_base import KnowledgeBaseController

router = APIRouter(prefix='/api')

router.include_router(AuthController.create_router())
router.include_router(UserController.create_router())
router.include_router(KnowledgeBaseController.create_router())
router.include_router(ChatController.create_router())
