import os
import cohere
from dotenv import load_dotenv

load_dotenv()

co = cohere.ClientV2(api_key=os.getenv("CO_API_KEY"))

user_input = input("Enter your prompt: ")

response = co.chat(
    model="command-r7b-12-2024",   
    messages=[
        {"role": "user", "content": user_input}
    ],
    max_tokens=200
)

print(response.message.content[0].text)


