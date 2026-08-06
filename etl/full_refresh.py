import pandas as pd
import psycopg
from datetime import datetime
import time

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


def copy_table(pg_conn, duck_conn, table):

    start = time.perf_counter()
    print(f"\nCopying {table}...")

    dataframe = pd.read_sql(
        f"SELECT * FROM {table}",
        pg_conn,
    )

    duck_conn.execute(
        f"DROP TABLE IF EXISTS {table}"
    )

    duck_conn.register(
        "temp_df",
        dataframe,
    )

    duck_conn.execute(
        f"""
        CREATE TABLE {table}
        AS
        SELECT *
        FROM temp_df
        """
    )
    duration = time.perf_counter() - start
    duck_conn.execute(
        """
        INSERT OR REPLACE INTO etl_metadata
        VALUES
        (
            ?,
            CURRENT_TIMESTAMP,
            (
                SELECT MAX(id)
                FROM temp_df
            ),
            ?,
            ?,
            ?
        )
        """,
        (
            table,
            "SUCCESS",
            len(dataframe),
            duration,
        ),
    )
    print(
        f"{table:<20}"
        f"{len(dataframe):>8} rows"
        f"{duration:>10.3f}s"
    )

    return len(dataframe)


def main():

    print("=" * 50)
    print("Full Refresh ETL")
    print("=" * 50)

    postgres = psycopg.connect(**POSTGRES)

    warehouse = get_connection()

    total_rows = 0

    for table in TABLES:

        total_rows += copy_table(
            postgres,
            warehouse,
            table,
        )

    postgres.close()

    warehouse.close()

    print("\n" + "=" * 50)
    print("ETL Completed")
    print("=" * 50)

    print(f"Tables copied : {len(TABLES)}")
    print(f"Rows copied   : {total_rows}")


if __name__ == "__main__":
    main()