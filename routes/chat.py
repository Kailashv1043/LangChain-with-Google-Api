from fastapi import APIRouter
from pydantic import BaseModel
import uuid

from services.chat_agent import chat_with_history

router = APIRouter()

class ChatRequest(BaseModel):
    message:str
    session_id:str | None=None

@router.post("/chat")
def chat(req:ChatRequest):
    session_id=req.session_id or str(uuid.uuid4())
    config={
        "configurable":{"session_id":session_id}
    }
    response=chat_with_history.invoke(
        {"input":req.message},
        config=config
    )
    return {
        "response":response.content,
        "session_id":session_id
    }