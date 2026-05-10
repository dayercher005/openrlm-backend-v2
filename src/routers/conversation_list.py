from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from src.models import Conversation, Message
from src.libs.database import get_session
from src.services.rlm_engine import RlmEngine
import asyncio

router = APIRouter()

@router.get("")
def list_conversations(session: Session = Depends(get_session)):
    return session.exec(select(Conversation)).all()


@router.get("/{conversation_id}")
async def get_conversation_with_messages(conversation_id: str, session: Session = Depends(get_session)):
    return session.exec(select(Conversation))

@router.post("/{conversation_id}")
async def create_message(message: str, conversation_id: str, session: Session = Depends(get_session)):
    RlmResponse = asyncio.run(RlmEngine(message))
    RlmMessage = Message(
        conversation_id=conversation_id, 
        role='ai', 
        content=RlmResponse
    )
    session.add(RlmMessage)
    session.commit()
    session.refresh(RlmMessage)
    return RlmMessage