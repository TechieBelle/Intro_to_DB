import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

connector = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),   
    password = os.getenv("DB_PASSWORD"),
    database = os.getenv("DB_NAME")
)
#connect to the database
cursor = connector.cursor()


def create_database():
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database created successfully.")
    except:
        print("Error creating database.")


connector.commit()
connector.close()
