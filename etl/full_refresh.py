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


def copy_table(pg_conn, duck_conn, table):

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

    print(f"Rows copied : {len(dataframe)}")

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