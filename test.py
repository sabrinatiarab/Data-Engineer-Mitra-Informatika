import mysql.connector
from db_config import DB_CONFIG

try:
    conn = mysql.connector.connect(
        database=DB_CONFIG['database'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        host=DB_CONFIG['host'],
        port=DB_CONFIG['port']
    )
    print("Connection successful!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if conn.is_connected():
        conn.close()
        print("Connection closed.")