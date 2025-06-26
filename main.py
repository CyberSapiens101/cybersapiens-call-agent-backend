from fastapi import FastAPI, Request
from chat_logic import process_chat

app = FastAPI()

@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    user_input = data.get("message", "")
    return {"response": process_chat(user_input)}
