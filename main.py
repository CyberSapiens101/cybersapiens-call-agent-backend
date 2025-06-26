from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from chat_logic import process_chat

app = FastAPI()

# Enable CORS to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or set your specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    user_input = data.get("user_input", "")
    bot_reply = process_chat(user_input)
    return {"bot_reply": bot_reply}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
