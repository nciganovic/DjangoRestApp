import pyautogui
import os 
import time
from dumy import *

pyautogui.FAILSAFE= True

title = (519, 739)

pyautogui.click(1919, 1071)
pyautogui.click(353, 1072)

for i in range(len(title_arr)):
    pyautogui.moveTo(519, 739, 2)
    time.sleep(1)
    pyautogui.click(title)
    pyautogui.typewrite('\t')
    pyautogui.typewrite(f'{title_arr[i]}\t', 0.1)
    pyautogui.typewrite(f'{rating_arr[i]}\t', 0.1)
    pyautogui.typewrite(f'{review_arr[i]}\t', 0.1)
    pyautogui.typewrite(f'{price_arr[i]}\t', 0.1)
    pyautogui.typewrite(f'{owner_arr[i]}\t\t', 0.1)
    pyautogui.typewrite(f'{link_arr[i]}\t', 0.1)
    pyautogui.typewrite(f'\n', 0.1)
    time.sleep(1)