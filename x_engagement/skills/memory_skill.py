import time

def run(user_input, memory):
    if "ingat" in user_input:
        fact = user_input.replace("ingat", "").strip()
        memory["user_facts"][str(time.time())] = fact
        return "Oke, sudah aku simpan di memori."

