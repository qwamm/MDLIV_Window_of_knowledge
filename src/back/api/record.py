from fastapi_controllers import Controller, get, post
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from src.database import get_db_session
from src.domain import RecordService, KnowBaseService
from pydantic import BaseModel


class AddRecordRequest(BaseModel):
    knowledge_base: int
    files: list[int]
    description: str
    tags: list[int]

class AddTagRequest(BaseModel):
    tag_name: str
    description: str
    record_ids: list[int]


class DeleteRecordRequest(BaseModel):
    kb_id: int
    id: int


class RecordResponse(BaseModel):
    knowledge_base: int
    files: list[int]
    description: str
    tags: list[int]


class RecordController(Controller):
    prefix = "/record"
    tags=["record"]

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session
        self.record_service = RecordService(session)
        self.knowbase_service = KnowBaseService(session)

    @get("/info")
    async def get_record(self, id: int) -> RecordResponse:
        record = await self.record_service.get_by_id(id)
        return RecordResponse(knowledge_base=record.knowbase, files=record.files, description=record.description,
                              tags=record.tags)

    @post("/add_record")
    async def add_record(self, request: AddRecordRequest):
        record = await self.record_service.create_record(request.description, request.files, request.tags)
        await self.knowbase_service.add_record(request.knowledge_base, record)
        return {"message": "OK"}

    @post("/delete_record")
    async def delete_record(self, request: DeleteRecordRequest):
        record = await self.record_service.get_by_id(request.id)
        await self.knowbase_service.delete_record(request.kb_id, record)
        return {"message": "OK"}

    @post("/add_tag")
    async def add_tag(self, request: AddTagRequest):
        await self.record_service.add_tag(request.tag_name, request.description, request.record_ids)
        return {"message": "OK"}

    @post("/delete_tag")
    async def delete_tag(self, tag_id: int):
        await self.record_service.delete_tag(tag_id)
        return {"message": "OK"}
