import mysql.connector as mysql

db = mysql.connect(
    host='localhost',
    user='root',
    password='root'
)


print(db)
