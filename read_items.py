import mysql.connector as mysql

connect = mysql.connect(
host = "localhost",
user = "root",
password = "root",
database = "walmart"
)

cursor = connect.cursor()

query = cursor.execute("SELECT * FROM products")
result = cursor.fetchall()

for i in result:
    print(i)

