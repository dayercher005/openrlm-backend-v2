import uuid

from sqlmodel import SQLModel

class MessageBase(SQLModel):
    role: str
    content: str
    
class MessageCreate(MessageBase):
    pass

class MessageOut(MessageBase):
    id: int
    conversation_id: uuid