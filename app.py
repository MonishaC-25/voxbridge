from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os

# --- Import AI/language functions ---
# Once Akshyaa pushes her real files into the ai/ folder,
# these imports will pull in the real functions automatically.
# Until then, the stubs below (at the bottom of this file) are used.
try:
    from ai.language_detect import detect_language
    from ai.ai_engine import get_ai_response
except ImportError:
    print("⚠️  ai/ module files not found yet — using local stub functions.")
    from stubs import detect_language, get_ai_response

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    try:
        detected_lang = detect_language(user_message)
        ai_reply = get_ai_response(user_message, detected_lang)
    except Exception as e:
        print(f"Error during processing: {e}")
        return jsonify({"error": "Something went wrong processing your message."}), 500

    return jsonify({
        "reply": ai_reply,
        "detected_language": detected_lang
    })


@app.route("/health")
def health():
    """Simple check to confirm the server is running."""
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True)
