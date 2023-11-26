import pyautogui

import webbrowser
webbrowser.open("https://bard.google.com/chat/5c9eb77ba658617e")
import time
time.sleep(4)
pyautogui.click(x=975, y=985)
pyautogui.typewrite("hello ho are you")
pyautogui.press('enter')
time.sleep(8)
pyautogui.click(x=1556, y=364)

