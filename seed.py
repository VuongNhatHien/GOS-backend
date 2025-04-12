import csv
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

def insert_csv_to_mysql(csv_file_path, table_name):
    try:
        load_dotenv()

        db_config = {
            'host': os.getenv('DB_HOST'),
            'database': os.getenv('DB_NAME'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD')
        }

        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()
            print("Connected to MySQL database")

            with open(csv_file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                csv_headers = next(csv_reader)

                db_headers = ['id' if h == 'sbd' else h for h in csv_headers]

                columns = ', '.join(db_headers)
                placeholders = ', '.join(['%s'] * len(db_headers))
                insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

                for row in csv_reader:
                    try:
                        processed_row = [None if val == '' else val for val in row]
                        cursor.execute(insert_query, processed_row)
                    except Error as e:
                        print(f"Error inserting row {row}: {e}")
                        continue

                connection.commit()
    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")

csv_file_path = 'scores.csv'  # Replace with your CSV file path
table_name = 'scores'

insert_csv_to_mysql(csv_file_path, table_name)