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
cursor = connection.cursor(buffered=True)


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


def get_products():
    get_products_query = 'SELECT product_name FROM prices;'
    cursor.execute(get_products_query)
    products = [product[0] for product in cursor.fetchall()]
    return products


def fetch_id_from_db(product):
    get_product_id_query = 'SELECT product_id FROM prices WHERE product_name=%s;'
    cursor.execute(get_product_id_query, (product,))
    product_id = cursor.fetchone()[0]
    return product_id


def get_max_product_id():
    get_max_id_query = 'SELECT MAX(product_id) FROM prices;'
    cursor.execute(get_max_id_query)
    max_id = cursor.fetchone()[0]
    return max_id