import pyautogui
from art import *
import win32api as winner
import threading
from time import sleep

click = bool(0) # Initialize click as False initially
points = 0
        
def button_click():
    global click
    pyautogui.moveTo(960, 540)
    while True:
        x, y = pyautogui.position()
        while winner.GetKeyState(0x01) < 0 and 70 <= x <= 360 and 100 <= y <= 195:
            click = bool(1)  # Set click to True
            break
        continue

print(button_art)

def check():
    global click
    global points
    while True:
        if click:
            print(print_number(points))
            click = False
            points += 1
        else:
            continue

threading.Thread(target=check).start()
threading.Thread(target=button_click).start()
