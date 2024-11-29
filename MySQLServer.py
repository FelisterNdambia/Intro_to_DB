import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Your MySQL server's host
            user='root',       # Your MySQL username
            password='password'  # Your MySQL password
        )

        if connection.is_connected():
            print("Connected to MySQL server")
            cursor = connection.cursor()
            
            # Try creating the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Run the function
create_database()

