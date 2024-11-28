from notion_client import Client
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict
from src.database import File, Record
from src.database import FileRepository


class NotionService:
    def __init__(self, notion_token: str, file_repo: FileRepository):

        self.notion_client = Client(auth=notion_token)
        self.file_repo = file_repo

    async def get_page_text_content(self, page_id: str) -> str:

        blocks = self.notion_client.blocks.children.list(page_id=page_id)["results"]
        text_content = []

        for block in blocks:
            if "type" in block and block["type"] == "paragraph":
                paragraph = block["paragraph"]
                if "text" in paragraph:
                    for text in paragraph["text"]:
                        text_content.append(text["plain_text"])

        return "\n".join(text_content)

    async def get_files_from_page(self, page_id: str) -> List[Dict[str, str]]:

        blocks = self.notion_client.blocks.children.list(page_id=page_id)["results"]
        files = []

        for block in blocks:
            if "type" in block and block["type"] == "file":
                file_block = block["file"]
                files.append({
                    "type": "file",
                    "url": file_block["file"]["url"]
                })
            elif "type" in block and block["type"] == "image":
                image_block = block["image"]
                files.append({
                    "type": "image",
                    "url": image_block["file"]["url"]
                })

        return files

    async def save_files_from_page(self, page_id: str, record: Record) -> List[File]:

        files_data = await self.get_files_from_page(page_id)
        saved_files = []

        for file_data in files_data:
            file = await self.file_repo.add_file(
                type=file_data["type"],
                URL=file_data["url"],
                keywords=[],
                record=record
            )
            saved_files.append(file)

        return saved_files