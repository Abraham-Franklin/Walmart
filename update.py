import mysql.connector as mysql

connect = mysal.connect(
host = "localhost",
user = "root",
password = "root",
database = "walmart",
)

cursor = connect.cursor()

query_stmt = f"UPDATE walmart SET price = {price} WHERE name = {name} VALUES ('{price}', '{name}'')"

cursor.execute(query_stmt)

cursor.commit()

cursor.close()
connect.close()