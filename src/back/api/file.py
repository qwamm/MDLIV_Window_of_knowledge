import json
from http.client import HTTPException
import os
from select import select

from fastapi_controllers import Controller, get, post
from importlib_metadata import files
from pydantic import BaseModel
from fastapi import Depends, Response
from sqlalchemy.sql.coercions import expect
from watchfiles import awatch

from src.domain import FileService, KnowBaseService, RecordService
from src.database import User, Record, RecordRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_db_session
from datetime import timedelta
from fastapi import UploadFile
from src.domain import s3_connection
from src.domain.s3_connection import S3Client
from starlette.status import HTTP_400_BAD_REQUEST
from fastapi import File, UploadFile, Depends, HTTPException
from fastapi.responses import FileResponse
from src.enviroments import s3_access_key, s3_secret_key, s3_endpoint, s3_bucket

client = S3Client(
    access_key=s3_access_key,
    secret_key=s3_secret_key,
    endpoint_url=s3_endpoint,
    bucket_name=s3_bucket
)

class addFileRequest(BaseModel):
    record_name: str
    file: UploadFile
    files_descripton: str


class FileController(Controller):
    prefix="/file"
    tags=["file"]

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session
        self.file_service = FileService(session)
        self.knowbase_service = KnowBaseService(session)
        self.records_service = RecordService(session)

    @post("/addFile")
    async def addFiles(self, response: UploadFile, kb_id: int, record_id: int):
        if response is None:
            raise HTTPException(HTTP_400_BAD_REQUEST, 'incorrect files')
        else:
            knowbase = await self.knowbase_service.get_by_id(kb_id)
            url = await client.upload_file(response, where=knowbase.name)
            try:
                await self.records_service.get_by_id(record_id)
                await self.records_service.add_file(file_url=url, description="", record_id=record_id)
                return {"message": "OK", "url": f"{url}", "isCreateNewRecord": False, "recordId": record_id}
            except:
                stmt = await self.records_service.create_record(description="", tag_ids=[],
                                                         knowbase_id=kb_id, file_ids=[])
                await self.records_service.add_file(file_url=url, description="", record_id=stmt.id)
                return {"message": "OK", "url" : f"{url}", "isCreateNewRecord" : True, "recordId": record_id}

    @get("/getFiles")
    async def get_files(self, bucket_name: str, file_name: str):
        file_path = await client.get_file(file_name)
        if file_path is not None:
            return FileResponse(path=file_path)
        else:
            raise HTTPException(HTTP_400_BAD_REQUEST, file_path)

    @get("/getFilesKnowbase")
    async def get_files_from_knowbase(self, knowbase_name : str):
        return await client.get_files_in_knowbase(knowbase_name)



