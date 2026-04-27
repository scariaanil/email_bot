import os

from dotenv import load_dotenv
from google import genai

load_dotenv()
API_KEY = os.getenv("API_KEY_GEMINI")
client = genai.Client(api_key=API_KEY)

# This lists all models your current API key can access
for model in client.models.list():
    print(model.name)


try:
    print("Sending single request...")
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents="Write a one sentence joke about Python.",
    )
    print("Success!\n", response.text)
except Exception as e:
    print(f"Error: {e}")
