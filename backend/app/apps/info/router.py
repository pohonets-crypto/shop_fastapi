import socket

from fastapi import APIRouter
from app.settings import settings

from .schemas import BaseBackendInfoSchema, BaseDatabaseInfoSchema

info_router = APIRouter()

@info_router.get("/backend")
async def get_backend_info() -> BaseBackendInfoSchema:
    """Get current backend info"""
    return {"backend": socket.gethostname()}


@info_router.get("/database")
async def get_database_info() -> BaseDatabaseInfoSchema:
    """Get current database info"""
    return BaseDatabaseInfoSchema(database_url=settings.DATABASE_ASYNC_URL)


