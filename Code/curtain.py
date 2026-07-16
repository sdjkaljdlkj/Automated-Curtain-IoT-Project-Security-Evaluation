from motor import *

state = "CLOSED"

def open_curtain():
    global state
    if state == "CLOSED":
        Backwards()
        state = "OPEN"
    return state

def close_curtain():
    global state
    if state == "OPEN":
        Forwards()
        state = "CLOSED"
    return state

