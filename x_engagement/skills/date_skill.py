from datetime import datetime

def run(user_input, memory):
    if "tanggal" in user_input:
        return datetime.now().strftime("Hari ini %d %B %Y")

