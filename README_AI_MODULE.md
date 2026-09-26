# VoxBridge — AI & Language Module (ai-module branch)

## What's in here

- `ai/language_detect.py` — detects the language of the user's message using **Langid**
- `ai/ai_engine.py` — sends the message to **Google Gemini** (free tier) and returns a reply
  in the same language

## Before you start

Make sure you're on the `ai-module` branch in GitHub Desktop (check the branch dropdown
at the top — switch to it if it says `main` or something else).

## Setup

1. Pull the latest `main` first, so you have Monisha's `app.py` already in place:
   - GitHub Desktop → switch to `main` → Fetch origin → Pull origin
   - Then switch back to `ai-module` → Branch menu → "Update from main" (or merge main into
     your branch) so your branch has `app.py`, `requirements.txt`, `.gitignore`, etc.

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create your own `.env` file (same format as `.env.example` in the repo):
   ```
   GEMINI_API_KEY=your_actual_key_here
   ```
   Get a free key at **aistudio.google.com** → "Get API key" → "Create API key".
   (You can use your own key, or ask Monisha for the shared team key — either works.)

## Where these files go

Create a folder named exactly `ai` inside your `voxbridge` project folder, and put both
files inside it:
```
voxbridge/
└── ai/
    ├── language_detect.py
    └── ai_engine.py
```
This matches exactly what `app.py` is already expecting to import — no other setup needed.

## How to test your files BEFORE plugging into the full app

Each file can be run directly on its own, to sanity-check it works:

```
python ai/language_detect.py
```
You should see several example sentences printed along with their detected language codes.

```
python ai/ai_engine.py
```
You should see a natural-language reply printed in the terminal (in English, since the
test message is in English).

## How to test the FULL app with your real files plugged in

Once both files are in place inside `ai/`:

```
python app.py
```
Then open `http://127.0.0.1:5000` in your browser. Since `app.py` automatically prefers
your real `ai/` files over the stub functions, you should now get REAL Gemini-generated
replies instead of the placeholder "(stub reply)" text.

You can also test the `/chat` route directly:
```
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d "{\"message\": \"Bonjour, comment ça va?\"}"
```
Expected: a French-language reply, with `"detected_language": "fr"`.

## Once it's working: commit and push

In GitHub Desktop (on the `ai-module` branch):
1. Confirm `.env` does NOT appear in the Changes list (it should be ignored)
2. Type a commit message: `Added language detection and Gemini AI engine`
3. Click **Commit to ai-module**
4. Click **Push origin**
5. On github.com, click **Compare & pull request** → **Create pull request** → **Merge pull request** → **Confirm merge**

After merging, everyone pulls the latest `main` and the whole app should work end-to-end
with real AI replies.
