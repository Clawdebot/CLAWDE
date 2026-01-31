from ai_engine import ask_ai
from crypto_skill import get_crypto_price
from parser import parse_command

print("🤖 AI Bot Aktif... ketik 'exit' untuk keluar\n")

while True:
    user_msg = input("Kamu: ")

    if user_msg.lower() == "exit":
        break

    cmd, data = parse_command(user_msg)

    if cmd == "price":
        response = get_crypto_price(data)
    else:
        response = ask_ai(data)

    print("Bot:", response)

