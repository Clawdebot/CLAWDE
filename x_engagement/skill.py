import time
import json
import requests

# ================= MEMORY =================
def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except:
        return {"history": [], "mood": "neutral", "personality": "santai"}

def save_memory(memory):
    with open("memory.json", "w") as f:
        json.dump(memory, f)

memory = load_memory()

# ================= AI (OpenRouter) =================
OPENROUTER_API_KEY = "API_KEY"
MODEL = "openai/gpt-4o-mini"

def ask_ai(message):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": f"Kamu AI. Mood: {memory['mood']}"},
            {"role": "user", "content": message}
        ]
    }
    res = requests.post("https://openrouter.ai/api/v1/chat/completions",
                        headers=headers, json=data)
    return res.json()["choices"][0]["message"]["content"]

# ================= COMMANDS =================
def handle_command(text):
    if text.strip().lower() == "/reset":
        memory["history"] = []
        save_memory(memory)
        return "🧠 Memory direset."
    if text.lower().startswith("/mode "):
        mode = text.split(" ",1)[1]
        memory["personality"] = mode
        save_memory(memory)
        return f"🎭 Personality diset ke {mode}"
    if text.lower() == "/status":
        return f"📊 Mood: {memory['mood']} | Personality: {memory.get('personality','santai')}"
    return None

# ================= MAIN FUNCTION =================
def ai_reply(user_text):
    # cek command
    cmd = handle_command(user_text)
    if cmd:
        return cmd

    # update mood
    lower = user_text.lower()
    if any(w in lower for w in ["capek","lelah","sedih"]):
        memory["mood"] = "tired"
    elif any(w in lower for w in ["anjir","mantap","seru"]):
        memory["mood"] = "excited"
    else:
        memory["mood"] = "neutral"

    # save history
    memory["history"].append({"role":"user","content":user_text})
    memory["history"] = memory["history"][-10:]  # simpan 10 terakhir

    # ask AI
    reply = ask_ai(user_text)

    memory["history"].append({"role":"assistant","content":reply})
    save_memory(memory)

    return reply

