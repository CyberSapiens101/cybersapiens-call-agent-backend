from fastapi import FastAPI
from pydantic import BaseModel
from chat_logic import process_chat

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "CyberSapiens Call Agent Backend is running!"}

@app.post("/chat")
def chat_endpoint(chat_request: ChatRequest):
    return {"response": process_chat(chat_request.message)}
