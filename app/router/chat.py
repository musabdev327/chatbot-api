# routers/chat.py
from fastapi import APIRouter
from pydantic import BaseModel
from fuzzywuzzy import process
import random
import nltk

nltk.download('punkt')

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

RESPONSES = {
    "hello": ["Hello! How can I help you today?", "Hi there! Need assistance?"],
    "how are you": ["I'm doing great! How about you?", "I'm here to help!"],
    "what is your name": ["I am your chatbot assistant!", "You can call me ChatBot!"],
    "thank you": ["You're welcome!", "Glad I could help!"],
    "bye": ["Goodbye! Have a great day!", "See you next time!"]
}

def get_response(user_message):
    """Match user message with best response using fuzzy matching"""
    user_message = user_message.lower().strip()
    best_match, score = process.extractOne(user_message, RESPONSES.keys())
    
    if score > 70:
        return random.choice(RESPONSES[best_match])
    
    return "I'm not sure I understand. Can you rephrase?"

@router.post(
    "/chat",
    tags=["chat"],
    response_model=ChatResponse,
    summary="Chat with the bot",
    response_description="Bot's response to user messages"
)
def chat(request: ChatRequest) -> ChatResponse:
    response = get_response(request.message)
    return ChatResponse(response=response)
