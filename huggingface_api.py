import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_API_KEY"),
)

user_input = input("Enter your prompt: ")

completion = client.chat.completions.create(
    model="MiniMaxAI/MiniMax-M2.5:novita",
    messages=[
        {
            "role": "user",
            "content": user_input
        }
    ],
    max_tokens=500
)


print("Full response:", completion)
print("---")
print("Message:", completion.choices[0].message.content)