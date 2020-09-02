import mysql.connector as mysql
from mysql.connector import errorcode
from settings import host, user, password, database

try:
    db = mysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
except mysql.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Something is wrong with your username or password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Database does not exist')
    else:
        print(err)

cursor = db.cursor()

# cursor.execute('CREATE DATABASE price_scraper;')  # just for initial DB create
# cursor.execute('SHOW DATABASES;')  # check existing databases
cursor.execute('CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255));')

cursor.execute('CREATE TABLE IF NOT EXISTS prices (id INT AUTO_INCREMENT PRIMARY KEY, '
               'product_id INT NOT NULL,'
               'scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, '
               'price FLOAT,'
               'FOREIGN KEY(product_id) REFERENCES products(id));')
# cursor.execute('SHOW TABLES;')  # check if tables were created


def insert_product(title: str):
    insert_product_statement = 'INSERT INTO products (title) VALUES (%s);'
    cursor.execute(insert_product_statement, (title,))
    db.commit()


def insert_price(price: float, product_id: int):
    insert_price_statement = 'INSERT INTO prices (price, product_id) VALUES (%s, %s);'
    cursor.execute(insert_price_statement, (price, product_id))
    db.commit()

