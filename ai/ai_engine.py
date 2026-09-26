# ai/ai_engine.py
#
# Sends the user's message to Google Gemini and returns an AI-generated
# reply in the SAME language the user wrote in.
#
# Requires GEMINI_API_KEY to be set in the .env file.
# Uses the current "google-genai" package (the old "google-generativeai"
# package and gemini-2.0-flash model name are both retired).

import os
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("⚠️  GEMINI_API_KEY not found in .env — ai_engine will not work until it's set.")

client = genai.Client(api_key=api_key) if api_key else None

# "gemini-flash-latest" is an alias that always points to Google's current
# best Flash model — using this instead of a specific version number means
# this code won't break again when Google retires/renames models.
MODEL_NAME = "gemini-flash-latest"


def get_ai_response(text: str, lang: str) -> str:
    """
    Sends the user's message to Gemini and asks it to reply in the
    same language (given by the detected language code, e.g. 'en', 'ta').

    Returns the AI's reply as plain text.
    """
    if not client:
        return "AI engine is not configured — missing GEMINI_API_KEY."

    prompt = (
        f"You are a helpful, polite customer support assistant. "
        f"The customer's message is written in language code '{lang}'. "
        f"Reply naturally and ONLY in that same language, "
        f"in a friendly and professional customer-support tone.\n\n"
        f"Customer message: {text}"
    )

    # Free-tier Gemini models occasionally return 503 "high demand" errors.
    # Retry a few times with a short pause before giving up.
    max_attempts = 3
    wait_seconds = 2

    for attempt in range(1, max_attempts + 1):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )
            return response.text.strip()

        except Exception as e:
            print(f"AI response generation failed (attempt {attempt}/{max_attempts}): {e}")
            if attempt < max_attempts:
                time.sleep(wait_seconds)
                wait_seconds *= 2  # wait a bit longer each retry
            else:
                return "Sorry, I'm having trouble responding right now. Please try again."


# --- Quick manual test ---
# Run this file directly (python ai/ai_engine.py) to sanity-check it
# before plugging it into the rest of the app.
if __name__ == "__main__":
    test_message = "What are your working hours?"
    test_lang = "en"
    print(get_ai_response(test_message, test_lang))
