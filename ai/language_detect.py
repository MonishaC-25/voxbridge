# ai/language_detect.py
#
# Detects the language of the user's message using Langid.
# Called from app.py for every incoming chat message.

import langid


def detect_language(text: str) -> str:
    """
    Detects the language of the given text.

    Returns a language code, e.g. 'en' (English), 'ta' (Tamil),
    'hi' (Hindi), 'fr' (French), etc.

    Falls back to 'en' if detection fails or the text is empty.
    """
    if not text or not text.strip():
        return "en"

    try:
        lang_code, confidence = langid.classify(text)
        return lang_code
    except Exception as e:
        print(f"Language detection failed: {e}")
        return "en"


# --- Quick manual test ---
# Run this file directly (python ai/language_detect.py) to sanity-check it
# before plugging it into the rest of the app.
if __name__ == "__main__":
    samples = [
        "Hello, how are you?",
        "Bonjour, comment ça va?",
        "வணக்கம், எப்படி இருக்கீங்க?",
        "नमस्ते, आप कैसे हैं?",
    ]
    for s in samples:
        print(f"{s!r} -> {detect_language(s)}")
