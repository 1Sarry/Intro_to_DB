import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    port=3306,
    password='$@ry0556'
)
cursor = mydb.cursor()


sql_script="""

CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

CREATE TABLE Authors(
author_id INT PRIMARY KEY,
author_name VARCHAR(251)
);

CREATE TABLE Books(
book_id INT PRIMARY KEY,
title VARCHAR(130),
author_id INT,
price DOUBLE,
publication_date DATE,
FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

CREATE TABLE Customers(
 customer_id INT PRIMARY KEY,
 customer_name VARCHAR(215),
 email VARCHAR(215),
 address TEXT
);

CREATE TABLE Orders (
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE,
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Order_Details(
orderdetailid INT PRIMARY KEY,
quantity DOUBLE,
order_id INT,
book_id INT,
FOREIGN KEY (order_id) REFERENCES Orders(order_id),
FOREIGN KEY (book_id) REFERENCES Books(book_id)
);
"""

statements = sql_script.split(';')
try:
    for stmt in statements:
        stmt = stmt.strip()
        if stmt: 
            cursor.execute(stmt)
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")

cursor.close()
mydb.close()
