import secrets
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from werkzeug.security import check_password_hash, generate_password_hash

from ..models import File, KnowBase


class FileRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session