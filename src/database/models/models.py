from __future__ import annotations
from sqlalchemy import String, ForeignKey, Table, Column
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime


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


class AccessPolicy(Base):
    __tablename__ = "access_policies"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    ip_addresses: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)
    policy: Mapped[bool] = mapped_column(nullable=False, default=False)

    user: Mapped[User] = relationship("User", back_populates="access_policies")

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str]
    second_name: Mapped[str | None]

    knowbases: Mapped[list[KnowBase]] = relationship(
        back_populates="users", secondary=knowbase_users_table
    )
    access_policies: Mapped[list[AccessPolicy]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


class File(Base):
    __tablename__ = "file"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    type: Mapped[str]
    URL: Mapped[str] = mapped_column(nullable=False)
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
    customization: Mapped["Customization"] = relationship(back_populates="knowbase")
    search_logs: Mapped[list["SearchLog"]] = relationship(back_populates="knowbase")
    integrations: Mapped[list["ExternalIntegration"]] = relationship(back_populates="knowbase")


class UsersBase(Base):
    __tablename__ = "usersbase"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    roles: Mapped[list[int]] = mapped_column(ARRAY(Mapped[int]))


class Customization(Base):
    __tablename__ = "customization"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    knowbase_id: Mapped[int] = mapped_column(ForeignKey("knowbase.id"), nullable=False)
    font: Mapped[str]
    logo_URL: Mapped[str]

    knowbase: Mapped["KnowBase"] = relationship(back_populates="customization")


class SearchLog(Base):
    __tablename__ = "search_log"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    knowbase_id: Mapped[int] = mapped_column(ForeignKey("knowbase.id"))
    query: Mapped[str] = mapped_column(nullable=False)
    timestamp: Mapped[datetime] = mapped_column(nullable=False)

    user: Mapped["User"] = relationship(back_populates="search_logs")
    knowbase: Mapped["KnowBase"] = relationship(back_populates="search_logs")

''' здесь я бы подумал 
class ExternalIntegration(Base):
    __tablename__ = "external_integration"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    type: Mapped[str] = mapped_column(nullable=False)
    token: Mapped[str] = mapped_column(nullable=True)
    knowbase_id: Mapped[int] = mapped_column(ForeignKey("knowbase.id"), nullable=False)

    knowbase: Mapped["KnowBase"] = relationship(back_populates="integrations")
'''

