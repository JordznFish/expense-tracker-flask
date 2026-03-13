import psycopg2
from config import Config

# def get_db_connection():
#     #Create a new db connection
#     conn = psycopg2.connect(os.getenv("DATABASE_URL"))
#     return conn

def get_db_connection():
    try:
        conn = psycopg2.connect(Config.DATABASE_URL)
        return conn
    except Exception as e:
        print("Database connection error:", e)
        return None
