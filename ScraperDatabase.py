import mysql.connector as mysql
from mysql.connector import errorcode
from settings import user, password

try:
    db = mysql.connect(
        host='localhost',
        user=user,
        password=password
    )
except mysql.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Something is wrong with your username or password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Database does not exist')
    else:
        print(err)
else:
    db.close()

