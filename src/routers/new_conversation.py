from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from src.libs.database import get_session
from src.models import Conversation, Message
from src.services.rlm_engine import RlmEngine 
import asyncio

router = APIRouter()

@router.get("")
def get_conversation_creator(conversation_id: str, session: Session = Depends(get_session)):
    conversation = session.get(Conversation, conversation_id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return session.exec(
        select(Message).where(Message.conversation_id == conversation_id)
    ).all()


@router.post("")
def create_conversation(title: str, session: Session = Depends(get_session)):
    conversation = Conversation(title=title)
    session.add(conversation)
    RlmResponse = asyncio.run(RlmEngine(title))
    RlmMessage = Message(
        conversation_id=conversation.conversation_id, 
        role='ai', 
        content=RlmResponse
    )
    session.add(RlmMessage)
    session.commit()
    session.refresh(conversation)
    return conversation