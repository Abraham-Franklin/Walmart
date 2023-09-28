import mysql.connector as mysql

connect = mysql.connect(
host = "localhost",
user = "root",
password = "root",
)

cursor = connect.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS walmart")

cursor.execute("USE walmart")

stmt = cursor.execute("""CREATE TABLE products (
product_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(30) NOT NULL UNIQUE,
brand VARCHAR(30),
price INT(8) NOT NULL,
stock_quantity INT(5) NOT NULL,
specs VARCHAR(100),
date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)""")

query = cursor. execute("""CREATE TABLE sales(
sales_id INT AUTO_INCREMENT PRIMARY KEY,
quantity_sold INT,
price INT,
product_id INT,
FOREIGN KEY (product_id) REFERENCES products(product_id)
)""")

connect.commit()
print("Database and Table creation successful ")
connect.close()
cursor.close()

