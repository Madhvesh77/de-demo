from pathlib import Path
import pandas as pd
import psycopg

from warehouse.connection import get_connection

POSTGRES = {
    "host": "localhost",
    "port": 5432,
    "dbname": "shopsmart",
    "user": "admin",
    "password": "shopsmart123",
}

TABLES = [
    "customers",
    "categories",
    "products",
    "inventory",
    "orders",
    "order_items",
    "payments",
]


def initialize():

    warehouse = get_connection()

    schema = Path("warehouse/schema.sql").read_text()

    warehouse.execute(schema)

    postgres = psycopg.connect(**POSTGRES)

    for table in TABLES:

        print(f"Creating {table}")

        df = pd.read_sql(
            f"SELECT * FROM {table} LIMIT 0",
            postgres,
        )

        warehouse.register(
            "temp_schema",
            df,
        )

        warehouse.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table}
            AS
            SELECT *
            FROM temp_schema
            """
        )

    postgres.close()
    warehouse.close()


if __name__ == "__main__":
    initialize()