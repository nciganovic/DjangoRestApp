import pyautogui
import os 
import time
#import scrape
import dumy

top_down = (1919, 1071)
browser_icon = (248, 1071)
search_in_browser = (156, 69)
product_link = (574, 529)

link = 'https://rest-project-amazon.herokuapp.com/\n'

pyautogui.click(top_down)
pyautogui.click(browser_icon) #click on browser icon
pyautogui.click(search_in_browser)
pyautogui.typewrite(link, 0.05)
time.sleep(2)
pyautogui.click(product_link)
time.sleep(1)
pyautogui.click(product_link)

for i in range(3):
    pyautogui.typewrite('\t')

pyautogui.typewrite(f'{dumy.title_arr[0]} \t')
pyautogui.typewrite(f'{dumy.rating_arr[0]} \t')
pyautogui.typewrite(f'{dumy.review_arr[0]} \t')
pyautogui.typewrite(f'{dumy.price_arr[0]} \t')
pyautogui.typewrite(f'{dumy.owner_arr[0]} \t')
pyautogui.typewrite(f'\t')
pyautogui.typewrite(f'{dumy.link_arr[0]} \t')
pyautogui.typewrite(f'\n')