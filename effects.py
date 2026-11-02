import time
def typewriter(text, delay=0.02):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()