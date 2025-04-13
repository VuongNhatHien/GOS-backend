import csv
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import time

def insert_csv_to_mysql(csv_file_path, table_name, batch_size=5000):
    try:
        load_dotenv()

        db_config = {
            'host': os.getenv('DB_HOST'),
            'port': int(os.getenv('DB_PORT', 3306)),
            'database': os.getenv('DB_NAME'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD')
        }

        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()
            print("Connected to MySQL")

            with open(csv_file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                csv_headers = next(csv_reader)
                db_headers = ['id' if h == 'sbd' else h for h in csv_headers]

                columns = ', '.join(db_headers)
                placeholders = ', '.join(['%s'] * len(db_headers))
                insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

                batch = []
                total_inserted = 0
                start_time = time.time()

                for i, row in enumerate(csv_reader, 1):
                    processed_row = [None if val == '' else val for val in row]
                    batch.append(processed_row)

                    if len(batch) == batch_size:
                        cursor.executemany(insert_query, batch)
                        connection.commit()
                        total_inserted += len(batch)
                        print(f"Inserted {total_inserted:,} rows...")
                        batch.clear()

                # Insert remaining rows
                if batch:
                    cursor.executemany(insert_query, batch)
                    connection.commit()
                    total_inserted += len(batch)
                    print(f"Inserted {total_inserted:,} rows (final batch)")

                duration = time.time() - start_time
                print(f"Done! Inserted {total_inserted:,} rows in {duration:.2f} seconds.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("SQL connection closed.")

# Run the seeder
insert_csv_to_mysql('scores.csv', 'scores')
