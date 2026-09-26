# stubs.py
# Temporary placeholder functions so the backend can run and be tested
# BEFORE Akshyaa's real ai/language_detect.py and ai/ai_engine.py exist.
#
# Delete this file (or just stop importing it) once the real ai/ files
# are merged into main from the ai-module branch.


def detect_language(text: str) -> str:
    """Fake language detector — always returns English for now."""
    return "en"


def get_ai_response(text: str, lang: str) -> str:
    """Fake AI reply — just echoes the message back."""
    return f"(stub reply) You said: {text}"
