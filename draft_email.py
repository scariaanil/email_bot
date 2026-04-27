import os

from dotenv import load_dotenv
from google import genai

from summary import email_prompt

# 1. Load environment variables and initialize the client
load_dotenv()
API_KEY = os.getenv("API_KEY_GEMINI")
client = genai.Client(api_key=API_KEY)


def draft_email():
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite", contents=email_prompt
        )
        if response.text:
            # print(response.text)
            return response.text.replace("**", "")

        else:
            return

    except Exception as e:
        print(f"An error occurred: {e}")


print("\n" + "-" * 50)
