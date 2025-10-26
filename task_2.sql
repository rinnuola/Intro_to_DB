import mysql.connector

# Replace with your actual MySQL credentials
username = "yourusername"
password = "yourpassword"

try:
    # 1️⃣ Connect without specifying a database first
    mydb = mysql.connector.connect(
        host="localhost",
        user=username,
        password=password
    )

    mycursor = mydb.cursor()

    # 2️⃣ Create the database if it doesn't exist
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

    # 3️⃣ Optionally, switch to the new database
    mycursor.execute("USE alx_book_store")
    print("Using database 'alx_book_store'.")

except mysql.connector.Error as e:
    print(f"Failed to connect to MySQL or execute command! Error: {e}")

finally:
    if 'mydb' in locals() and mydb.is_connected():
        mycursor.close()
        mydb.close()
