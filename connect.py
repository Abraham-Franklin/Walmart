import mysql.connector

connect = mysql.connector.connect(
host = "localhost",
user = "root",
password = "root",
)

cursor = connect.cursor()

query = cursor.execute("CREATE DATABASE walmart")
print(query)