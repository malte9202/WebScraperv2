import requests  # http-requests
from bs4 import BeautifulSoup  # scraping
from ScraperDatabase import *


url = 'https://geizhals.de/?cat=tvlcd&xf=2728_DVB-S2%7E34_3840x2160%7E4546_55'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 '
                  '(KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'
}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')


def get_title():
    productlinks = soup.find_all('a', {'class': 'productlist__link'})
    count = 0
    while count < len(productlinks):
        title = productlinks[count].find('span').get_text(strip=True)
        insert_product(title)
        count += 1


get_title()


def get_price():
    prices = soup.find_all('span', {'class': 'gh_price'})
    count = 0
    while count < len(prices):
        price = float(prices[count].find('span').get_text(strip=True)[2:].replace(",", "."))
        insert_price(price, count+1)
        count += 1


get_price()
