from ScraperDatabase import connect, create_table, insert, fetch_id_from_db, get_products, get_max_product_id
from WebScraper import get_product_names, get_prices, get_product_id

# set up db connection
connect()

# create database table
create_table()

for product in get_product_names():
    product_name = product
    if product_name in get_products():  # check for product_name in DB -> take this id
        product_id = fetch_id_from_db(product_name)
    elif product_name in get_product_names():  # check for product_name in scrape result -> take this id
        product_id = get_product_id(get_product_names(), product_name)
    else:  # create new id if the product_name was not found in DB or scrape result
        product_id = get_max_product_id()+1
    price = get_prices(get_product_names())[product_id][1]
    insert(product_id, product_name, price)



