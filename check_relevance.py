import os
import re

from dotenv import load_dotenv
from google import genai

# from openai import OpenAI
from summary import relevance_prompt

# 1. Load variables from the .env file
load_dotenv()
API_KEY = os.getenv("API_KEY_GEMINI")

if not API_KEY:
    raise ValueError("API Key not found. Please check your .env file.")

# 3. Configure the Gemini SDK
client = genai.Client(api_key=API_KEY)
print("Setup complete. Client initialized successfully.")


def get_relevance_score():
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite", contents=relevance_prompt
        )
        usage = response.usage_metadata
        if not usage:
            return 0

        print("\n--- API Usage Monitor ---")
        print(
            f"Tokens Used: {usage.total_token_count} (Prompt: {usage.prompt_token_count})"
        )

        if not response or not response.text:
            print("Warning: Received empty response from AI.")
            return 0

        # Extract only the numerical score using Regex for robust parsing
        score_match = re.search(r"\d+", response.text.strip())
        if score_match:
            print(f"The relevance Score for the Profile is: {score_match.group()}")
            return int(score_match.group())

    except Exception as e:
        print(f"AI Error: {e}")
        return 0
