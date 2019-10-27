from bs4 import BeautifulSoup
#import datetime
#from tinydb import TinyDB, Query
import urllib3
import time
#import xlsxwriter

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #ignore SSL sertificate

url = 'https://www.amazon.com/Dri-Fit-Training-Athletic-Essentials-Undershirt/dp/B07J2QWHY4/ref=sr_1_2_sspa?crid=1B2U37K00A1OH&keywords=t-shirts+for+men&qid=1572206033&sprefix=t-s%2Caps%2C270&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNE5GUDRQUlFMMVI4JmVuY3J5cHRlZElkPUEwMDA4NjA4MjlVUlVWQjdLVERVSCZlbmNyeXB0ZWRBZElkPUEwMTE5MDk2NUtUTTVQUllERzYmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

def make_soup(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    return BeautifulSoup(r.data, 'lxml')

soup = make_soup(url)

#time.sleep(5)
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