from __future__ import annotations
from sqlalchemy import String, ForeignKey, Table, Column
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy.dialects.postgresql import ARRAY


class Base(DeclarativeBase):
    pass


knowbase_users_table = Table(
    "knowbase_users",
    Base.metadata,
    Column("knowbase_id", ForeignKey("knowbase.id"), primary_key=True),
    Column("user_id", ForeignKey("user.id"), primary_key=True),
)


record_files_table = Table(
    "record_files",
    Base.metadata,
    Column("record_id", ForeignKey("record.id"), primary_key=True),
    Column("file_id", ForeignKey("file.id"), primary_key=True),
)


record_tags_table = Table(
    "record_tags",
    Base.metadata,
    Column("record_id", ForeignKey("record.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str]
    second_name: Mapped[str]

    knowbases: Mapped[list[KnowBase]] = relationship(
        back_populates="users", secondary=knowbase_users_table
    )


class File(Base):
    __tablename__ = "file"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    type: Mapped[str]
    path: Mapped[str] = mapped_column(nullable=False)
    keywords: Mapped[list[str]] = mapped_column(ARRAY(String))

    records: Mapped[list[Record]] = relationship(
        secondary=record_files_table, back_populates="files"
    )


class Tag(Base):
    __tablename__ = "tag"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tag_name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None]

    records: Mapped[list[Record]] = relationship(
        secondary=record_tags_table, back_populates="tags"
    )


class Record(Base):
    __tablename__ = "record"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    description: Mapped[str | None]

    files: Mapped[list[File]] = relationship(
        secondary=record_files_table, back_populates="records"
    )
    tags: Mapped[list[Tag]] = relationship(
        secondary=record_tags_table, back_populates="records"
    )


class KnowBase(Base):
    __tablename__ = "knowbase"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None]

    users: Mapped[list[User]] = relationship(
        back_populates="knowbases", secondary=knowbase_users_table
    )


class UsersBase(Base):
    __tablename__ = "usersbase"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Mapped[int], ForeignKey("user.id"))
    roles: Mapped[list[int]] = mapped_column(ARRAY(Mapped[int]))
