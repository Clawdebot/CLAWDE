from datetime import datetime

def run(user_input, memory):
    if "jam" in user_input or "waktu" in user_input:
        return f"Sekarang jam {datetime.now().strftime('%H:%M')}"

