from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.models import Conversation, Message

from routers.new_conversation import router as new_conversation_router
from routers.conversation_list import router as conversation_list_router

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
    return {"message": "Hello World"}

app.include_router(new_conversation_router, prefix="/")
app.include_router(conversation_list_router, prefix="/conversations")