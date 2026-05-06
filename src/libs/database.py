from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine,  AsyncSession
from sqlalchemy.orm import sessionmaker

from src.config import PG_USER, PG_PASSWORD, PG_HOST, PG_PORT, PG_DATABASE

DATABASE_URL = f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"

# Engine for database
engine = create_async_engine(DATABASE_URL, echo=True)

# Session Generator for database
AsyncSessionLocal = sessionmaker(
    engine, class_ = AsyncSession, expire_on_commit=False
)


# Dependency Injection to get session in routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session