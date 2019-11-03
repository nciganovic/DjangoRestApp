import pyautogui
import os 
import time
#from dumy import *
from scrape import title_arr, rating_arr, review_arr, price_arr, owner_arr, links

pyautogui.FAILSAFE= True

#pyautogui.click(1919, 1071)
#pyautogui.click(353, 1072)

#RESOLUTION 1920x1080, LEFT HALF OF WINDOW NEEDS TO BE https://rest-project-amazon.herokuapp.com/products/
#FIRST CREATE ONE PROJECT INSANCE BY YOURSELF AND THEN RUN PROGRAM 

for i in range(len(title_arr)):
    if(i == 0):
        title = (438, 743)
        pyautogui.moveTo(438, 743, 1)
    else:
        title = (475, 757)
        pyautogui.moveTo(475, 757, 1)
    time.sleep(1)
    pyautogui.click(title)
    pyautogui.typewrite('\t')
    pyautogui.typewrite(f'{title_arr[i]}\t')
    pyautogui.typewrite(f'{rating_arr[i]}\t')
    pyautogui.typewrite(f'{review_arr[i]}\t')
    pyautogui.typewrite(f'{price_arr[i]}\t')
    pyautogui.typewrite(f'{owner_arr[i]}\t\t')
    pyautogui.typewrite(f'{links[i]}\t')
    pyautogui.typewrite(f'\n', 0.1)
    time.sleep(1)