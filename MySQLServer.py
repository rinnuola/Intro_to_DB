#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None  # initialize connection variable

    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",           # change this to your MySQL username
            password="#0halakW3@lth1__!!"  # change this to your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn’t exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close database connection safely
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection closed.")  # optional

if __name__ == "__main__":
    create_database()
