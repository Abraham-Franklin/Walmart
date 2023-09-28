import mysql.connector as mysql

connect = mysql.connect(
host = "localhost",
user = "root",
password = "root",
database = "walmart",
)

cursor = connect.cursor()

while True:
    name = input("Enter product name: ").strip()
    brand = input("Enter brand name: ").strip()
    specs = input("Enter product specs: ").strip()
    price = input("Enter price: ").strip()
    stock_quantity = input("Enter quantity: ").strip()
    
    query_stmt = cursor.execute(f"INSERT INTO products (name, brand, price, stock_quantity, specs) VALUES ('{name}', '{brand}',  '{price}', '{stock_quantity}', '{specs}')")
    
    connect.commit()
    print("Insertion complete")
    
    response = input("""Do you want to input more data(Y/n)""")
    
    if response.lower() not in ["y", "yes"]:
        break
        
print("Have a nice day")