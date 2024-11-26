from fastapi_controllers import Controller, get, post
from pydantic import BaseModel


class CreateRequest(BaseModel):
    name: str
    records: list[int]
    users: list[int]
    description: str


class AddRecordRequest(BaseModel):
    knowledge_base: int
    files: list[str]
    description: str
    tags: list[int]


class DeleteRecordRequest(BaseModel):
    kb_id: int
    id: int


class AccessRequest(BaseModel):
    id: int
    kb_id: int


class KnowledgeBaseController(Controller):
    prefix = "/knowledge_base"

    def __init__(self):
        pass

    @get("/info")
    def info(self, kb_id: int):
        # return info from db
        pass

    @post("/create")
    def create(self, request: CreateRequest):
        # create KB in db
        return {"message": "OK"}

    @post("/add_record")
    def add_record(self, request: AddRecordRequest):
        # check permission and add record
        return {"message": "OK"}

    @post("/delete_record")
    def delete_record(self, request: DeleteRecordRequest):
        # check permission and delete record
        return {"message": "OK"}

    @post("/delete")
    def delete(self, kb_id: int):
        # again check permission and then delete knowledgebase from all subscribed users
        return {"message": "OK"}

    @post("/request_access")
    def request_access(self, request: AccessRequest):
        # pend access request for admin of this kb
        return {"message": "OK"}

    @post("/grant_access")
    def grant_access(self, request: AccessRequest):
        # grant access to user
        return {"message": "OK"}
