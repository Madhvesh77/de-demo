import pandas as pd
import psycopg
import duckdb

from warehouse.connection import get_connection

POSTGRES = {
    "host": "localhost",
    "port": 5432,
    "dbname": "shopsmart",
    "user": "admin",
    "password": "shopsmart123"
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

def get_last_loaded_id(
    warehouse,
    table,
):

    result = warehouse.execute(
        """
        SELECT COALESCE(last_loaded_id,0)

        FROM etl_metadata

        WHERE table_name=?
        """,
        (table,),
    ).fetchone()

    if result is None:

        return 0

    return result[0]

def copy_incremental(
    postgres,
    warehouse,
    table,
):

    checkpoint = get_last_loaded_id(
        warehouse,
        table,
    )

    print(
        f"{table:<20}"
        f"Checkpoint : {checkpoint}"
    )

    cursor = postgres.cursor()

    cursor.execute(
        f"""
        SELECT *
        FROM {table}
        WHERE id > %s
        """,
        (checkpoint,),
    )

    rows = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]

    dataframe = pd.DataFrame(
        rows,
        columns=columns,
    )

    if dataframe.empty:

        print("No new rows.\n")

        return

    warehouse.register(
        "temp_df",
        dataframe,
    )

    warehouse.execute(
        f"""
        INSERT INTO {table}

        SELECT *

        FROM temp_df
        """
    )

    last_loaded_id = int(dataframe["id"].max())
    rows_loaded = int(len(dataframe))

    warehouse.execute(
        """
        UPDATE etl_metadata

        SET
            last_loaded_id=?,
            rows_loaded=rows_loaded+?,
            last_loaded_at=CURRENT_TIMESTAMP

        WHERE table_name=?
        """,
        (
            last_loaded_id,
            rows_loaded,
            table,
        ),
    )
    print(
        f"Copied {len(dataframe)} rows.\n"
    )

def main():

    postgres = psycopg.connect(**POSTGRES)

    warehouse = get_connection()

    print("="*60)

    print("Incremental ETL")

    print("="*60)

    for table in TABLES:

        copy_incremental(
            postgres,
            warehouse,
            table,
        )

    postgres.close()

    warehouse.close()


if __name__=="__main__":

    main()