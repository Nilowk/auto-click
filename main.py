from pynput.keyboard import Key, Listener
import mouse
import time

activated = False;

def on_press(key):
    if str(key) == "p":
        global activated
        activated = True if activated == False else False


with Listener(
        on_press=on_press) as listener:
    listener.join()

while True:
    if activated:
        mouse.click("left")
        time.sleep(0.01)