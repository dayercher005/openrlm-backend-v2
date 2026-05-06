from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from src.libs.database import get_db

router = APIRouter()

@router.get("")
async def get_conversations_list(db: AsyncSession = Depends(get_db)):
    
    return