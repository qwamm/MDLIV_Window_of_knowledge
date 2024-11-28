import json
from http.client import HTTPException
import os

from fastapi_controllers import Controller, get, post
from pydantic import BaseModel
from fastapi import Depends, Response
from src.domain import FileService
from src.database import User
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_db_session
from datetime import timedelta
from fastapi import UploadFile
from src.domain import s3_connection
from src.domain.s3_connection import S3Client
from starlette.status import HTTP_400_BAD_REQUEST
from fastapi import File, UploadFile, Depends, HTTPException
from fastapi.responses import FileResponse

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
        if response is None:
            raise HTTPException(HTTP_400_BAD_REQUEST, 'incorrect files')
        else:
            url = []
            for file in response.files:
                url += await client.upload_file(file)
            return {"message": "OK", "url" : f"{url}"}

    @get("/getFiles")
    async def get_files(self, bucket_name: str, file_name: str):
        file_path = await client.get_file(file_name)
        if file_path is not None:
            return FileResponse(path=file_path)
        else:
            raise HTTPException(HTTP_400_BAD_REQUEST, file_path)


