from warehouse.connection import get_connection


def build():

    conn = get_connection()

    conn.execute(
        "CREATE SCHEMA IF NOT EXISTS silver"
    )

    conn.execute(
        """
        DROP TABLE IF EXISTS silver.customer_orders
        """
    )

    conn.execute(
        """
        CREATE TABLE silver.customer_orders AS

        SELECT

            o.id                 AS order_id,

            o.created_at          AS order_created_at,

            o.status,

            c.id                 AS customer_id,

            c.first_name,

            c.city,

            p.id                 AS product_id,

            p.name               AS product_name,

            oi.quantity,

            oi.amount

        FROM bronze.orders o

        JOIN bronze.customers c
            ON o.customer_id = c.id

        JOIN bronze.order_items oi
            ON oi.order_id = o.id

        JOIN bronze.products p
            ON p.id = oi.product_id
        """
    )

    conn.execute(
        """
        DROP TABLE IF EXISTS silver.customer_payments
        """
    )

    conn.execute(
        """
        CREATE TABLE silver.customer_payments AS

        SELECT

            p.id                 AS payment_id,

            p.order_id,

            o.customer_id,

            c.first_name,

            p.amount,

            p.status,

            p.created_at

        FROM bronze.payments p

        JOIN bronze.orders o
        ON p.order_id = o.id

        JOIN bronze.customers c
        ON c.id = o.customer_id
        """
    )

    conn.close()


if __name__ == "__main__":
    build()