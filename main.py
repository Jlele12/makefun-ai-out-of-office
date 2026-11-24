REPLY = (
    "I'm out of office all week. My backlog dreams of me. Requests will be "
    "triaged by the auto-reply you are reading, which is also on vacation."
)

def main():
    reply = REPLY
    assert 1 <= len(reply) <= 159, len(reply)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(reply)

if __name__ == "__main__":
    main()
