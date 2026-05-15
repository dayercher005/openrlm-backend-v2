from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from src.models.models import Conversation, Message
from src.libs.database import get_session
from src.services.rlm_engine import RlmEngine
import asyncio

router = APIRouter()

@router.get("")
def list_conversations(session: Session = Depends(get_session)):
    return session.exec(select(Conversation)).all()

@router.delete("")
def delete_conversation(conversation_id: str ,session: Session = Depends(get_session)):
    selected_conversation = select(Conversation).where(Conversation.id == conversation_id)
    return session.delete(selected_conversation)

@router.get("/{conversation_id}")
async def get_conversation_with_messages(conversation_id: str, session: Session = Depends(get_session)):
    selected_conversation = select(Conversation).where(Conversation.id == conversation_id)
    return session.exec(selected_conversation)

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

@router.delete("/{conversation_id}")
async def delete_conversation(conversation_id: str, session: Session = Depends(get_session)):
    selected_conversation = select(Conversation).where(Conversation.id == conversation_id)
    return session.delete(selected_conversation)

@router.put("/{conversation_id}")
async def update_conversation(conversation_id: str, updated_title: str, session: Session = Depends(get_session)):
    selected_conversation = select(Conversation).where(Conversation.id == conversation_id).with_for_update()
    selected_conversation.title = updated_title
    session.commit()
    