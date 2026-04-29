import re
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
API_KEY = os.getenv("API_KEY_GEMINI")

if not API_KEY:
    raise ValueError("API Key not found. Please check your .env file.")

client = genai.Client(api_key=API_KEY)

def get_ai_response(prompt, task_type="text"):
    """
    Sends a prompt to Gemini and parses the response.
    :param prompt: The string prompt to send.
    :param task_type: "text" for drafted emails, "score" for relevance integers.
    """
    try:
        # 1. Make the API Call
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite", 
            contents=prompt
        )
        
        # 2. Universal API Usage Monitor
        usage = response.usage_metadata
        if usage:
            print("\n--- API Usage Monitor ---")
            print(f"Tokens Used: {usage.total_token_count} (Prompt: {usage.prompt_token_count})")

        # 3. Check for empty response
        if not response or not response.text:
            print("Warning: Received empty response from AI.")
            return 0 if task_type == "score" else None

        raw_text = response.text.strip()

        # 4. Handle Response Parsing based on task type
        if task_type == "score":
            # Extract only the numerical score
            score_match = re.search(r"\d+", raw_text)
            if score_match:
                score = int(score_match.group())
                print(f"The relevance Score for the Profile is: {score}")
                return score
            return 0
            
        elif task_type == "text":
            # Return email string with markdown bold tags stripped
            return raw_text.replace("**", "")

    except Exception as e:
        print(f"AI Error: {e}")
        return 0 if task_type == "score" else None