from engine import *
import threading

def Engine():
    threading.Timer(5, Engine).start()
    cycle()
Engine()