import time
def typewriter(text, delay=0.05):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()