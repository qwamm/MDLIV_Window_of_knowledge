import json
import os.path

from fastapi_controllers import Controller, get, post
from pydantic import BaseModel
from fastapi import Depends, Response
from ..login_manager import login_manager
from src.domain import UserService, KnowBaseService
from src.database import User
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_db_session
from datetime import timedelta
from src.ML import Assistant, ETL
from qdrant_client import QdrantClient
from src.domain import S3Client
from src.enviroments import s3_access_key, s3_secret_key, s3_endpoint, s3_bucket
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


client = S3Client(
    access_key=s3_access_key,
    secret_key=s3_secret_key,
    endpoint_url=s3_endpoint,
    bucket_name=s3_bucket
)


class MessageRequest(BaseModel):
    user_request: str
    kb_id: int


class LlmResponse(BaseModel):
    llm_response: str
    sources: list[str]


class ChatController(Controller):
    prefix = "/chat"
    tags=["chat"]

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.client = client
        self.knowbase_service = KnowBaseService(session)

    @post("/message")
    async def message(self, request: MessageRequest) -> LlmResponse:
        knowbase = await self.knowbase_service.get_by_id(request.kb_id)

        files = await self.client.get_files_in_knowbase(knowbase.name)
        for file in files:
            await self.client.get_file(file, directory=knowbase.name)

        # print([os.path.join(Path(__file__).parent.parent.parent.parent, knowbase.name, f) for f in os.listdir(knowbase.name)])

        qclient = QdrantClient(":memory:")
        etl = ETL([os.path.join(Path(__file__).parent.parent.parent.parent, knowbase.name, f) for f in os.listdir(knowbase.name)],
                  qclient)
        etl.etl(knowbase.name)

        assistant = Assistant(etl.loader.client)
        answr = assistant.answer(request.user_request)
        return LlmResponse(llm_response=answr["llm_response"], sources=answr["sources"])
