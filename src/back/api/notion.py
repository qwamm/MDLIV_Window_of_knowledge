from fastapi import APIRouter, HTTPException, Depends
from fastapi_controllers import Controller, get, post
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from starlette.responses import FileResponse
from notion_client import Client
import os
import uuid

from src.database import get_db_session
from src.domain import NotionService


class PageContentResponse(BaseModel):
    page_id: str
    title: str
    preview: str

class DownloadResponse(BaseModel):
    message: str
    file_path: str

class NotionController(Controller):
    prefix = "/notion"
    tags = ["notion"]

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session
        self.notion_service = NotionService(session)


    @post("/getUserPages")
    async def get_user_pages(self):
        notion_client = self.notion_service.notion_client
        results = notion_client.search(filter={"value": "page", "property": "object"})["results"]

        pages = []
        for page in results:
            title = "Untitled"
            if "properties" in page and "title" in page["properties"]:
                title_data = page["properties"]["title"]["title"]
                if len(title_data) > 0:
                    title = title_data[0]["plain_text"]
            pages.append(
                PageContentResponse(
                    page_id=page["id"],
                    title=title,
                    preview=f"First words: {title[:50]}..."
                )
            )
        return pages

    @post("/downloadPageContent")
    async def download_page_content(self, page_id: str) -> DownloadResponse:
        text_content = await self.notion_service.get_page_text_content(page_id)
        if not text_content:
            raise HTTPException(status_code=404, detail="Page content is empty or could not be retrieved.")

        file_name = f"{uuid.uuid4().hex}.txt"
        file_path = os.path.join("downloads", file_name)
        os.makedirs("downloads", exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_content)

        return DownloadResponse(message="File created successfully", file_path=file_path)



    @post("/set-token")
    async def set_integration_token(token: str):
        try:
            notion_service = NotionService(token, file_repo=None)
            notion_client = notion_service.notion_client
            notion_client.search()
            return {"message": "Token successfully validated and set."}
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Failed to validate token: {str(e)}")

    @get("/pages", response_model=List[PageContentResponse])
    async def get_pages(token: str):
        notion_service = NotionService(token, file_repo=None)
        notion_controller = NotionController(notion_service)
        return await notion_controller.get_user_pages()

    @get("/download/{page_id}", response_model=DownloadResponse)
    async def download_page(page_id: str, token: str):
        notion_service = NotionService(token, file_repo=None)
        notion_controller = NotionController(None, notion_service)
        download_response = await notion_controller.download_page_content(page_id)
        return download_response

    @get("/download-file/{file_path}")
    async def download_file(file_path: str):
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="File not found.")
        return FileResponse(file_path, media_type="text/plain", filename=os.path.basename(file_path))