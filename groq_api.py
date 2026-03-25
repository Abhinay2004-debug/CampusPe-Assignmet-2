import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

try:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    user_input = input("Enter your prompt: ")

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": user_input}],
        model="llama-3.3-70b-versatile"
    )

    print(response.choices[0].message.content)

except Exception as e:
    print("Error:", e)