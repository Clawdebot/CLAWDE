from brain import think
from skills.posting import make_post
from skills.reply import make_reply

def run_agent():
    decision = think()

    if decision == "post":
        make_post()
    elif decision == "reply":
        make_reply()
    else:
        print("Agent is resting...")

if __name__ == "__main__":
    run_agent()
