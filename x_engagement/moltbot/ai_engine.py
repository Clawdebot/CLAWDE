import requests
import json

with open("config.json") as f:
    config = json.load(f)

API_KEY = config["api_key"]
MODEL = config["model"]
SYSTEM_PROMPT = config["system_prompt"]

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def ask_ai(message):
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message}
        ]
    }

    try:
        r = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=60
        )
        res = r.json()
        return res["choices"][0]["message"]["content"]
    except Exception as e:
        return f"AI Error: {e}"
