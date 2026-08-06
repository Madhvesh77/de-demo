from dotenv import load_dotenv
import os
import psycopg

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

load_dotenv(ROOT_DIR / ".env")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def get_connection():
    return psycopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )


def test_connection():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT version();")

    version = cursor.fetchone()

    print(version[0])

    cursor.close()

    connection.close()


if __name__ == "__main__":

    test_connection()