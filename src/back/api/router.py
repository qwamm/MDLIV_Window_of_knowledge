from fastapi import APIRouter

from .notion import NotionController
from .auth import AuthController
from .user import UserController
from .chat import ChatController
from .knowledge_base import KnowledgeBaseController
from .record import RecordController
from .file import FileController

router = APIRouter(prefix='/api')

router.include_router(AuthController.create_router())
router.include_router(UserController.create_router())
router.include_router(KnowledgeBaseController.create_router())
router.include_router(ChatController.create_router())
router.include_router(RecordController.create_router())
router.include_router(FileController.create_router())
router.include_router(NotionController.create_router())
