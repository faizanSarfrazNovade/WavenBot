from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api,win32con # PIP INSTALL PYWIN32 FOR THIS
# pip install opencv-python aswellq

time.sleep(2)

def click(x,  y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

pyautogui.displayMousePosition()


#  963 952
# i = 0 
# nbClick = 0
# while i < 8 :
#     x = 582 + i * 110
#     y = 741
#     imageLocation = pyautogui.locateOnScreen("equiped.png", region=(x,y,100,100), grayscale=True, confidence=0.8)
#     if imageLocation != None:
#         print("equiped in position " + str(i+1))
#         click(x+20,y+20)
#         nbClick += 1
#     if i == 7 and nbClick == 1:
#         click(x+20,y+20)
#     i += 1