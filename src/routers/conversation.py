from fastapi import APIRouter, Request, Depends
from fastapi.responses import StreamingResponse

from sqlalchemy.ext.asyncio import AsyncSession

from sse_starlette.sse import EventSourceResponse

router = APIRouter()
    
@router.get("")
async def get_conversation(request: Request):
    return EventSourceResponse()