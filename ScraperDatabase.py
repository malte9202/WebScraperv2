import sqlite3

connection = sqlite3.connect('scraper.db')
cursor = connection.cursor()

create_table_products = 'CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, title TEXT)'


def create_table(query: str):
    cursor.execute(query)
    connection.commit()


create_table(create_table_products)


def insert_product(title: str):
    cursor.execute('INSERT INTO products(title) VALUES (?);', title)
    connection.commit()


insert_product('Testprodukt')
