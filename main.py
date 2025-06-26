from fastapi import FastAPI
from chat_logic import process_chat

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "CyberSapiens Call Agent Backend is running!"}

@app.post("/chat")
def chat_endpoint(user_input: dict):
    user_message = user_input.get("message", "")
    return {"response": process_chat(user_message)}
