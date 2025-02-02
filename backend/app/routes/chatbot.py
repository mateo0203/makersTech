from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.services.chatbot_service import chatbot_response

router = APIRouter()

# Define Pydantic model for request body
class ChatRequest(BaseModel):
    user_message: str

@router.post("/chat")
def chatbot_query(request: ChatRequest):
    print(f"Received message: {request.user_message}")  # Debugging
    response = chatbot_response(request.user_message)
    print(f"Response: {response}")  # Debugging
    return {"response": response}