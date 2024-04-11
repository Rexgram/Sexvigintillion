import pyautogui
from art import *
import win32api as winner
import threading
from time import sleep
import os

click = False  # Initialize click as False initially
points = 0
incremented = False  # Flag to track whether points have been incremented for the current mouse press event

def button_click():
    global click, incremented
    pyautogui.moveTo(960, 540)
    while True:
        x, y = pyautogui.position()
        mouse_pressed = winner.GetKeyState(0x01) < 0  # Check if left mouse button is pressed
        if mouse_pressed and 70 <= x <= 360 and 100 <= y <= 195:
            if not incremented:  # If points haven't been incremented yet for this press
                click = True  # Set click to True to indicate a valid press
                incremented = True  # Set incremented to True to prevent further incrementing
        elif not mouse_pressed:
            click = False  # Reset click to False when left mouse button is released
            incremented = False  # Reset incremented flag when button is released

os.system('cls' if os.name == 'nt' else 'clear')
print(button_art)

def check():
    global click, points
    while True:
        if click:
            points += 500
            os.system('cls' if os.name == 'nt' else 'clear')
            print_number(points)
            click = False  # Reset click after incrementing points

threading.Thread(target=check).start()
threading.Thread(target=button_click).start()