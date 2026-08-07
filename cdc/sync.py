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


def sync_payment(payment_id: int):

    print(f"Syncing payment {payment_id}")

    postgres = psycopg.connect(**POSTGRES)
    warehouse = get_connection()

    payment = pd.read_sql(
        """
        SELECT *
        FROM payments
        WHERE id = %s
        """,
        postgres,
        params=(payment_id,),
    )

    if payment.empty:
        print(f"Payment {payment_id} not found")
        postgres.close()
        warehouse.close()
        return

    warehouse.execute(
        """
        DELETE FROM payments
        WHERE id = ?
        """,
        (payment_id,),
    )

    warehouse.register(
        "payment_df",
        payment,
    )

    warehouse.execute(
        """
        INSERT INTO payments
        SELECT *
        FROM payment_df
        """
    )

    warehouse.unregister("payment_df")

    postgres.close()
    warehouse.close()

    print(f"Payment {payment_id} synchronized")