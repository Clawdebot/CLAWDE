import random
import time

def human_delay():
    time.sleep(random.randint(2, 5))

def do_reply():
    human_delay()

    styles = [
        "santai",
        "semangat",
        "singkat",
        "bercanda"
    ]

    style = random.choice(styles)

    text = "Bot is replying to a comment"

    if style == "santai":
        text += " hehe"

    elif style == "semangat":
        text += " 🔥"

    elif style == "singkat":
        text = "Ok"

    elif style == "bercanda":
        text += " wkwk"

    print("🤖", text)

