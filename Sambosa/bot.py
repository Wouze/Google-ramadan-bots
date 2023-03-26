import keyboard, pyautogui

import win32api
import win32con
import time
import keyboard

# To get x y cords of some place on screen, open cmd and write the following:
"""
python
import pyautogui
pyautogui.displayMousePosition()
"""


def click(pos):
    win32api.SetCursorPos(pos)
    time.sleep(0.03)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def complete(type):
    click(type)
    for _ in range(7):
        click(lf)
        time.sleep(0.05)

meat = 'meat.png'
cheese = 'cheese.png'

lf = (1442, 585)
# X: 1319 Y:  284 RGB: ( 77,  71,  68)
met = (1247, 1588)
# X: 1397 Y:  270 RGB: ( 57,  58,  66)
ches = (1656, 1571)

# X: 1705 Y:  322 RGB: ( 44,  52,  58)

while not keyboard.is_pressed('q'):
    if pyautogui.locateOnScreen(meat, grayscale=True, confidence=0.8, region=(0, 0, 1800, 400)):
        complete(ches)
    elif pyautogui.locateOnScreen(cheese, grayscale=True, confidence=0.8, region=(0, 0, 1800, 400)):
        complete(ches)
    
    print('slep')

