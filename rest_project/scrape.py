from bs4 import BeautifulSoup
#import datetime
#from tinydb import TinyDB, Query
import urllib3
import time
#import xlsxwriter

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #ignore SSL sertificate

def make_soup(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    return BeautifulSoup(r.data, 'lxml')

amazon_link = 'https://www.amazon.com/'

url = 'https://www.amazon.com/s?k=laptop&ref=nb_sb_noss_2'

soup = make_soup(url)

tags = soup.find_all('a', {"class": "a-link-normal a-text-normal"})

links = []

for tag in tags:
    tag = str(tag) # => full tag
    index_of_href = tag.find('href') 
    tag_sup = tag[index_of_href + 6:] # => cutting everything up to href

    index_of_end = tag_sup.find('"')
    only_link = tag_sup[:index_of_end] # => cutting everything after ("), so i get only link

    working_link = only_link.replace('amp;', '') # => removing apm;

    full_link = amazon_link + working_link # => adding base amazon link to specific link

    #print(i, "-->", full_link, "\n")

    links.append(full_link)

print('############################## STARTING TO ENTER EACH LINK #############################\n')

title_arr = []
rating_arr = []
review_arr = []
price_arr = []
owner_arr = []

from random import random

num_of_links = len(links)

for idx, link in enumerate(links):
    
    print(f'-------------START ITEM NUMBER {idx}/{num_of_links} ------------- \n')

    value = (random() * 5) + 1
    print('Time sleep ', value)
    time.sleep(value)

    url = link

    soup = make_soup(url)

    have_all_items = True

    try:
        title = soup.find('span', {"id":"productTitle"}).text.strip()
        print('---> Title: ', title)
    except:
        title = 'Title not found!'
        have_all_items = False
        print('---> Title: ', title)

    try:
        rating = soup.find('span', {"class": "a-size-medium a-color-base"}).text[:3]
        if " " in rating:
            rating = rating[:1]
        print('---> Rating: ', rating)
    except:
        rating = 'Rating not found!'
        have_all_items = False
        print('---> Rating: ', rating)

    try:
        review = soup.find('span', {"id": "acrCustomerReviewText"}).text # => 68 ratings
        review_num_arr = review.split(" ")[:-1] # => ['68']
        review_num = review_num_arr[0] # => 68
        print('---> Review numbers: ', review_num)
    except: 
        review = 'Review not found!'
        have_all_items = False
        print('---> Review numbers: ', review_num)

    try:
        price = soup.find('span', {"id": "priceblock_ourprice"}).text
        price = price.replace("$", "")
        print('---> Price: ', price)
    except:
        price = 'Price not found!'
        have_all_items = False
        print('---> Price: ', price)

    try:
        owner = soup.find('a', {"id": "bylineInfo"}).text
        print('---> Owner: ', owner)
    except:
        owner = 'Owner not found!'
        have_all_items = False
        print('---> Owner: ', owner)

    print('\n--->Amazon link ', link, '\n')

    if(have_all_items):
        title_arr.append(title)
        rating_arr.append(rating)
        review_arr.append(review_num)
        price_arr.append(price)
        owner_arr.append(owner)
        print("\n Item appended!")
    else:
        print("\n Item not appended!")
        continue

    print(f'-------------END ITEM NUMBER {idx} ------------- \n')

print('\n############################## SCRAPE ENDED #############################\n')

print('------All titles------')
for idx, t in enumerate(title_arr):
    print(idx, t)

print('------All ratings------')

for idx, r in enumerate(rating_arr):
    print(idx, r)

print('------All reviews------')
for idx, rw in enumerate(review_arr):
    print(idx, rw)

print('------All price------')
for idx, p in enumerate(price_arr):
    print(idx, p)

print('------All owners------')
for idx, o in enumerate(owner_arr):
    print(idx, o)

'''
url = 'https://www.amazon.com/Dri-Fit-Training-Athletic-Essentials-Undershirt/dp/B07J2QWHY4/ref=sr_1_2_sspa?crid=1B2U37K00A1OH&keywords=t-shirts+for+men&qid=1572206033&sprefix=t-s%2Caps%2C270&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNE5GUDRQUlFMMVI4JmVuY3J5cHRlZElkPUEwMDA4NjA4MjlVUlVWQjdLVERVSCZlbmNyeXB0ZWRBZElkPUEwMTE5MDk2NUtUTTVQUllERzYmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

soup = make_soup(url)

try:
    title = soup.find('span', {"id":"productTitle"}).text.strip()
except:
    title = 'Title not found!'

try:
    rating = soup.find('span', {"class": "a-size-medium a-color-base"}).text[:3]
except:
    rating = 'Rating not found!' 
try:
    review = soup.find('span', {"id": "acrCustomerReviewText"}).text # => 68 ratings
    review_num_arr = review.split(" ")[:-1] # => ['68']
    review_num = review_num_arr[0] # => 68
except: 
    review = 'Review not found!'

try:
    price = soup.find('span', {"id": "priceblock_ourprice"}).text
    price = price.replace("$", "")
except:
    price = 'Price not found!'
try:
    owner = soup.find('a', {"id": "bylineInfo"}).text
except:
    owner = 'Owner not found!'

print('--------START SCRAPE------------\n')
print("Title: ",title)
print("\n")
print('Rating:', rating)
print("\n")
print('Review number:', review_num)
print("\n")
print('Price:', price)
print("\n")
print('Owner:', owner)
'''