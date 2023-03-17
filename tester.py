from main import t
import threading

def start2():
    threading.current_thread().run(t.playGame())
    t.playGame()
