from fastapi_controllers import Controller, get, post
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from src.domain import KnowBaseService, RecordService


class CreateRequest(BaseModel):
    name: str
    description: str


class AddRecordRequest(BaseModel):
    knowledge_base: int
    files: list[int]
    description: str
    tags: list[int]


class DeleteRecordRequest(BaseModel):
    kb_id: int
    id: int


class KnowBaseInfoResponse(BaseModel):
    name: str
    description: str


class KnowledgeBaseController(Controller):
    prefix = "/knowledge_base"
    tags=["knowledge_base"]

    def __init__(self, session: AsyncSession):
        self.session = session
        self.knowbase_service = KnowBaseService(session)
        self.record_service = RecordService(session)

    @get("/info")
    async def info(self, kb_id: int) -> KnowBaseInfoResponse:
        knowbase = await self.knowbase_service.get_by_id(kb_id)
        return KnowBaseInfoResponse(name=knowbase.name, description=knowbase.description)

    @post("/create")
    async def create(self, request: CreateRequest):
        knowbase = await self.knowbase_service.create_KnowBase(request.name, request.description)
        return {"message": "OK"}

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

    @post("/delete")
    async def delete(self, kb_id: int):
        await self.knowbase_service.delete_KnowBase(kb_id)
        return {"message": "OK"}

    # @post("/request_access")
    # def request_access(self, request: AccessRequest):
    #     # pend access request for admin of this kb
    #     return {"message": "OK"}
    #
    # @post("/grant_access")
    # def grant_access(self, request: AccessRequest):
    #     # grant access to user
    #     return {"message": "OK"}
