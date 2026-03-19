from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, mapped_column, declared_attr, Mapped
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.sql import func


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"
