from warehouse.connection import get_connection

TABLES = [
    "customers",
    "categories",
    "products",
    "inventory",
    "orders",
    "order_items",
    "payments",
]


def build():

    conn = get_connection()

    conn.execute(
        "CREATE SCHEMA IF NOT EXISTS bronze"
    )

    for table in TABLES:

        print(f"Copying {table}")

        conn.execute(
            f"DROP TABLE IF EXISTS bronze.{table}"
        )

        conn.execute(
            f"""
            CREATE TABLE bronze.{table}
            AS
            SELECT *
            FROM main.{table}
            """
        )

        for table in TABLES:

            conn.execute(
                f"DROP TABLE main.{table}"
            )

    conn.close()


if __name__ == "__main__":
    build()