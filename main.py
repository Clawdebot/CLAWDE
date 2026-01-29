from brain import think
from skills.posting import make_post
from skills.reply import check_replies

def run_agent():
    print("Clawde Agent Running...")

    decision = think()

    if decision == "post":
        make_post()
    elif decision == "reply":
        check_replies()
    else:
        print("Agent resting...")

if __name__ == "__main__":
    run_agent()
