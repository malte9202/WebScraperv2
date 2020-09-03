from ScraperDatabase import connect, create_table, insert
from WebScraper import get_product_names, get_prices, get_product_id

# set up db connection
connect()

# create database table
create_table()

for product in get_product_names():
    product_name = product
    product_id = int(get_product_id(get_product_names(), product))
    price = get_prices(get_product_names())[product_id][1]
    insert(product_id, product_name, price)
