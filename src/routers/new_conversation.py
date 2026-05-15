from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from src.libs.database import get_session
from src.models.models import Conversation, Message
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
def create_conversation(message: str, session: Session = Depends(get_session)):
    conversation = Conversation(title=message)
    user_message = Message(
        content=message,
        conversation_id = conversation.id,
        role='user'
    )
    session.add(conversation)
    session.add(user_message)
    rlm_response = asyncio.run(RlmEngine(message))
    rlm_message = Message(
        conversation_id=conversation.id, 
        role='ai', 
        content=rlm_response,
        conversation=conversation
    )
    session.add(rlm_message)
    session.commit()
    session.refresh(conversation)
    return conversation