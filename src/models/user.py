import uuid

from sqlmodel import Field, Relationship, SQLModel

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str = Field(default=None)
    password: str = Field(default=None)
    