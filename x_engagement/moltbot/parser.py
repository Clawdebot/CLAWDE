def parse_command(text):
    if text.startswith("/price "):
        coin = text.split(" ", 1)[1]
        return "price", coin

    return "chat", text
