import json
from http.client import HTTPException

from fastapi_controllers import Controller, get, post
from pydantic import BaseModel
from fastapi import Depends, Response
from ..login_manager import login_manager
from src.domain import FileService
from src.database import User
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_db_session
from datetime import timedelta
from fastapi import UploadFile
from src.domain import s3_connection
from ...domain.s3_connection import S3Client
from starlette.status import HTTP_400_BAD_REQUEST

client = S3Client(
    access_key="YCAJElPfE9y_wvK6_qcrWCqLU",
    secret_key="YCM2xdSph9Johvz2WzXJkbRsZf4dmqH65CIPuuLo",
    endpoint_url="https://storage.yandexcloud.net",
    bucket_name="aaaa-test"
)

class addFilesRequest(BaseModel):
    record_name: str
    files: list[UploadFile]
    files_descripton: list[str]


class FileController(Controller):
    prefix="/file"
    tags=["file"]

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session
        self.file_service = FileService(session)

    @post("/addFiles")
    async def addFiles(self, response: addFilesRequest):
        if response.files is None:
            raise HTTPException(HTTP_400_BAD_REQUEST, 'uncorrect files')
        else:
            for file in response.files:
                await client.upload_file(file)
            return {"message": "OK"}