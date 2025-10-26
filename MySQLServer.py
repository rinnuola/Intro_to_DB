import mysql.connector

# IMPORTANT: You must replace 'yourusername' and 'yourpassword' with your actual MySQL credentials.
# Note: If the database 'alx_book_store' does not exist yet, the connection 
# might fail because you are specifying it in the connection call.
# A common practice when creating a database is to connect without the 
# 'database' parameter, or connect to a default like 'mysql'.
try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="yourusername", # <--- REPLACE THIS
      password="yourpassword", # <--- REPLACE THIS
      database="alx_book_store"
    )

    mycursor = mydb.cursor()

    # This command attempts to create the database only if it doesn't exist
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    # This block catches connection or execution errors, such as wrong credentials
    print(f"Failed to connect to MySQL or create database! Error: {e}")

finally:
    # Close the cursor and connection to release resources
    if 'mydb' in locals() and mydb.is_connected():
        mycursor.close()
        mydb.close()
