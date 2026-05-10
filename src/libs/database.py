from sqlmodel import create_engine, Session
from sqlalchemy import create_engine

from src.config import PG_USER, PG_PASSWORD, PG_HOST, PG_PORT, PG_DATABASE

DATABASE_URL = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"

# Engine for database
engine = create_engine(DATABASE_URL, echo=True)

# Dependency Injection to get session in routes
async def get_session():
    with Session(engine) as session:
        yield session