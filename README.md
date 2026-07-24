# Chat Bot

Simple terminal chatbot using Google Gemini (`gemini-2.5-flash`) and Python.

## Setup

```bash
# clone & enter dir
git clone <repo-url>
cd "Chat Bot"

# create venv & activate
python3 -m venv .venv
source .venv/bin/activate

# install reqs
pip install -r requirements.txt
```

Put your Gemini API key in a `.env` file:

```env
GEMINI_API_KEY=your_key_here
```

## Run

```bash
python main.py
```

Type `bye` to exit.
