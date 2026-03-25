import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

try:
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    user_input = input("Enter your prompt: ")

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=user_input
    )

    print(response.text)

except Exception as e:
    print("Error:", e)