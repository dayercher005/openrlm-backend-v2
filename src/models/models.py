from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime
import uuid

class Conversation(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    title: str
    created_at: datetime = Field(default_factory=datetime.now)
    messages: List["Message"] = Relationship(back_populates="conversation")
    
class Message(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    conversation_id: str = Field(foreign_key="conversation.id")
    role: str  # "user" | "ai"
    content: str
    created_at: datetime = Field(default_factory=datetime.now)
    conversation: Conversation = Relationship(back_populates="messages")
    
class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    username: str = Field(default=None)
    password: str = Field(default=None)