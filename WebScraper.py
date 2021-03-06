import requests  # http-requests
from bs4 import BeautifulSoup  # scraping


url = 'https://geizhals.de/?cat=tvlcd&xf=2728_DVB-S2%7E34_3840x2160%7E4546_55'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 '
                  '(KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'
}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')


def get_product_names():
    productlinks = soup.find_all('a', {'class': 'productlist__link'})
    count = 0
    products = []
    while count < len(productlinks):
        product_name = productlinks[count].find('span').get_text(strip=True)
        products.append(product_name)
        count += 1
    return products


def get_prices(products):
    prices = soup.find_all('span', {'class': 'gh_price'})
    count = 0
    products_prices = []
    while count < len(prices):
        price = float(prices[count].find('span').get_text(strip=True)[2:].replace(",", "."))
        products_prices.append((products[count],price))
        count += 1
    return products_prices


def get_product_id(products, product_name):
    product_id = products.index(product_name)
    return product_id
