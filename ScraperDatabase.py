import mysql.connector as mysql
from settings import host, user, password, database


def connect():
    try:
        db = mysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return db
    except mysql.Error as err:
        print(err)


connection = connect()
cursor = connection.cursor()


def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS prices (id INT AUTO_INCREMENT PRIMARY KEY, '
                   'product_id INT NOT NULL,'
                   'product_name VARCHAR(255),'
                   'price FLOAT,'
                   'scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);')


def insert(product_id: int, product_name: str, price: float):
    insert_statement = 'INSERT INTO prices (product_id, product_name, price) VALUES (%s, %s, %s);'
    cursor.execute(insert_statement, (product_id, product_name, price))
    connection.commit()


