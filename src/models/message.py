import uuid

from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.conversation import Conversation

class Message(SQLModel, table=True):
    __table__name = "messages"
    
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    role: str = Field()
    content: str = Field(default=None)
    
    conversation_id: uuid.UUID = Field(foreign_key="conversations.id")
    conversation: Conversation = Relationship(back_populates="messages")