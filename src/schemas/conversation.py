import uuid

from sqlmodel import SQLModel
from typing import List
from src.schemas.message import MessageOut

class ConversationBase(SQLModel):
    title: str
    
class ConversationCreate(ConversationBase):
    pass

class ConversationOut(ConversationBase):
    id: uuid
    messages: List[MessageOut] = []