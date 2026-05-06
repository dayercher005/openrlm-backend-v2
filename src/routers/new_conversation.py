from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.libs.database import get_db
from src.models.models import Conversation

router = APIRouter()

@router.get("")
async def get_conversation(id, db: AsyncSession = Depends(get_db)):
    statement = select(Conversation).where(Conversation.id == id)
    existing_conversation = db.exec(statement).first()
    return existing_conversation

@router.post("")
async def create_conversation(db: AsyncSession = Depends(get_db)):
    new_conversation = Conversation.model_validate(
        
    )
    db.add(new_conversation)
    db.commit()
    db.refresh(new_conversation)
    return new_conversation