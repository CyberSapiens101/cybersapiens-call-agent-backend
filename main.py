from flask import Flask, request, jsonify
from chat_logic import process_chat

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "CyberSapiens Call Agent Backend is running."

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    reply = process_chat(user_input)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
