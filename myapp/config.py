import psycopg2
from psycopg2 import sql

# Function to get a database connection
def get_db_connection():
    """Returns a new database connection."""
    try:
        connection = psycopg2.connect(
            dbname="bank_db",  # Replace with your database name
            user="root",   # Replace with your database username
            password="", # Replace with your database password
            host="localhost",  # Replace with your database host, e.g. 'localhost'
            port="5432"        # Replace with your database port, e.g. '5432'
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

