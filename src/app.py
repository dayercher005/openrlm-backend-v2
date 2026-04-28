from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.models.models import Conversation, Message

from src.routers.new_conversation import router as new_conversation_router
from src.routers.conversation_list import router as conversation_list_router
from src.routers.conversation import router as conversation_router

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "OK"}

app.include_router(new_conversation_router, prefix="/new-conversation")
app.include_router(conversation_list_router, prefix="/conversations")
app.include_router(conversation_router, prefix="/conversations/{conversation_id}")