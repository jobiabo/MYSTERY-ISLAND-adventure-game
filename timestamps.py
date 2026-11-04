import threading
import queue

def timed_input(prompt, timeout=5):
    result = queue.Queue()

    def get_input():
        result.put(input(prompt))

    thread = threading.Thread(target=get_input, daemon=True)
    thread.start()

    try:
        return result.get(timeout=timeout).strip().lower()
    except queue.Empty:
        return None