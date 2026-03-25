import ollama
from dotenv import load_dotenv

load_dotenv()

user_input = input("Enter your prompt: ")

response = ollama.chat(
    model="gemma3:1b",   
    messages=[
        {"role": "user", "content": user_input}
    ]
)

print(response.message.content)