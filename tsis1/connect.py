import psycopg2
from config import DB_CONFIG


def connect():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Connected successfully")
        return conn
    except Exception as e:
        print("Not connected")
        print(e)
        return None
connect()