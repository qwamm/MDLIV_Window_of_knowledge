from ..engine import Base
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)


class KnowledgeBase(Base):
    __tablename__ = "knowledge_base"
    id: Mapped[int] = mapped_column(primary_key=True)


class UserBase(Base):
    __tablename__ = "user_base"
    id: Mapped[int] = mapped_column(primary_key=True)


class Record(Base):
    __tablename__ = "record"
    id: Mapped[int] = mapped_column(primary_key=True)


class File(Base):
    __tablename__ = "file"
    id: Mapped[int] = mapped_column(primary_key=True)


class Tag(Base):
    __tablename__ = "tag"
    id: Mapped[int] = mapped_column(primary_key=True)
