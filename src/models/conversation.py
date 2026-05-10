import uuid

from sqlmodel import SQLModel, Relationship, Field
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.message import Message

class Conversation(SQLModel, table=True):
    __table__name = "conversations"
    
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(default=None)
    
    messages: list["Message"] = Relationship(back_populates="conversation")