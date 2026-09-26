# VoxBridge — Backend Setup (backend branch)

## What's in here

- `app.py` — Flask server, defines the `/chat` route
- `stubs.py` — fake AI/language functions, used automatically if `ai/` files
  don't exist yet, so this can run and be tested independently
- `requirements.txt` — Python packages needed
- `.env.example` — template for your API key file (copy it to `.env`)
- `.gitignore` — keeps `.env` and junk files out of GitHub
- `templates/index.html` — placeholder page (Keerthana's real UI replaces this)

## How to run it locally

1. Install Python packages:
   ```
   pip install -r requirements.txt
   ```

2. Create your real `.env` file:
   ```
   cp .env.example .env
   ```
   Then open `.env` and paste in your real Gemini API key.

3. Run the server:
   ```
   python app.py
   ```

4. Open your browser to:
   ```
   http://127.0.0.1:5000
   ```
   You should see the placeholder page.

5. Test the chat route directly (without the frontend) using this command
   in a second terminal:
   ```
   curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d "{\"message\": \"hello\"}"
   ```
   You should get back a JSON reply like:
   ```
   {"reply": "(stub reply) You said: hello", "detected_language": "en"}
   ```

## When ai-module branch is merged

Once Akshyaa's `ai/language_detect.py` and `ai/ai_engine.py` exist in `main`,
`app.py` will automatically import the real functions instead of the stubs —
no code changes needed on your end. You can then delete `stubs.py`.

## When frontend branch is merged

Keerthana's real `templates/index.html`, `static/css/style.css`, and
`static/js/*.js` will replace the placeholder page automatically.
