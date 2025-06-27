from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chat_logic import process_chat

app = FastAPI()

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For testing; restrict in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "CyberSapiens Call Agent Backend is running!"}

@app.post("/chat")
def chat_endpoint(user_input: dict):
    user_message = user_input.get("message", "")
    return {"response": process_chat(user_message)}
