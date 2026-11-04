import uuid

from sqlalchemy import UUID, Column
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=60,
    pool_size=3,
    max_overflow=5,
)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass

class UUIDIdMixin:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
