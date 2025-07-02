import mysql.connector

from dotenv import load_dotenv
import os

load_dotenv()





def create_database():
    try:
        connector = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),   
            password = os.getenv("DB_PASSWORD")
            # database = os.getenv("DB_NAME")
        )
        #connect to the database
        cursor = connector.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database created successfully.")
        cursor.close()
        connector.close()
        print("Database connection closed.")
    except Exception as e:
        print("Error:", e)




if __name__ == "__main__":
    create_database()
  

