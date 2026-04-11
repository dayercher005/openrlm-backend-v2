import uuid

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

class Conversation(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(default=None)
    
    messages: list["Message"] = Relationship(back_populates="conversation")
    
class Message(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    role: str = Field()
    content: str = Field(default=None)
    
    conversation_id: uuid.UUID = Field(foreign_key="team.id")
    conversation: Conversation = Relationship(back_populates="messages")