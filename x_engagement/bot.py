import requests, json, time, os
import requests

# ===== LOAD CONFIG =====
with open("config.json") as f:
    cfg = json.load(f)

API_KEY = cfg["api_key"]
MODEL = cfg["model"]
SYSTEM_PROMPT = cfg["system_prompt"]

MEMORY_FILE = "memory.json"
LOG_FILE = "chatlog.txt"
COOLDOWN = 2

# ===== LOAD MEMORY =====
if os.path.exists(MEMORY_FILE):
    memory = json.load(open(MEMORY_FILE))
else:
    memory = {}

last_time = 0

# ===== HEADERS =====
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://localhost",
    "X-Title": "AI Platform V3"
}

def save_memory():
    json.dump(memory, open(MEMORY_FILE, "w"))

def log(text):
    with open(LOG_FILE, "a") as f:
        f.write(text + "\n")


def ask_ai(uid, msg):
    global last_time

    if time.time() - last_time < COOLDOWN:
        time.sleep(COOLDOWN)

    if uid not in memory:
        memory[uid] = [{"role": "system", "content": SYSTEM_PROMPT}]

    memory[uid].append({"role": "user", "content": msg})

    data = {"model": MODEL, "messages": memory[uid]}

    try:
        r = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
             json=data,
            timeout=60
        )
        res = r.json()

        if "error" in res:
            return f"API Error: {res['error']}"

        reply = res["choices"][0]["message"]["content"]
        memory[uid].append({"role": "assistant", "content": reply})

        save_memory()
        log(f"{uid}: {msg} -> {reply}")

        last_time = time.time()
        return reply

    except Exception as e:
        return f"System Error: {e}"

def token_skill(uid, token_name):
    prompt = f"""
Kamu adalah AI analis crypto profesional.

Buat analisa untuk token: {token_name}

Format WAJIB:

🔹 Ringkasan Proyek
🔹 Use Case
🔹 Kelebihan
🔹 Risiko
🔹 Kesimpulan AI (potensi jangka panjang)

Jawaban harus informatif tapi ringkas.
"""

    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        r = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=60
        )
        res = r.json()

        if "error" in res:
            return f"API Error: {res['error']}"

        return res["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Skill Error: {e}"



# ================= CRYPTO PRICE SKILL =================
    SYMBOL_MAP
def get_crypto_price(symbol):
    try:
        symbol = symbol.lower()

        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd&include_24hr_change=true"

        r = requests.get(url, timeout=10)
        data = r.json()

        if symbol not in data:
            return "❌ Koin tidak ditemukan."

        price = data[symbol]["usd"]
        change = data[symbol]["usd_24h_change"]

        arrow = "📈" if change > 0 else "📉"

        return f"💰 {symbol.upper()} Price: ${price}\n{arrow} 24h Change: {change:.2f}%"

    except Exception as e:
        return f"⚠️ Error ambil data crypto: {str(e)}"
# ======================================================


print("🧠 AI PLATFORM V3 FULL AKTIF\n")

while True:
    uid = input("User ID: ")
    msg = input("Pesan: ")

    if msg.lower() == "/reset":
        memory[uid] = [{"role": "system", "content": SYSTEM_PROMPT}]
        save_memory()
        print("Memory direset.")
        continue
    if msg.startswith("/price "):
            coin = msg.split(" ")[1]
            print("Bot:", get_crypto_price(coin))
            continue

    if msg.lower() == "exit":
        break

    print("Bot:", ask_ai(uid, msg))


