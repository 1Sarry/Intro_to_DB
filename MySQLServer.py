import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    port=3306,
    password='$@ry0556'
)
cursor = mydb.cursor()

with open("alx_book_store.sql", "r")as file:
    sql_script = file.read()
try:
    cursor.execute(sql_script)  
    print("SQL script execured successfully.") 
except mysql.connector.Error as err:
    print(f"Error: {err}")

cursor.close()
mydb.close()
