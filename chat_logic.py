import os
from openai import OpenAI
from dotenv import load_dotenv
print("DEBUG: OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def process_chat(user_input):
    try:
        response = client.chat.completions.create(
            model=os.getenv("MODEL_NAME", "gpt-4"),
            messages=[
                {"role": "system", "content": "You are a helpful assistant for CyberSapiens who answers WhatsApp queries."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
