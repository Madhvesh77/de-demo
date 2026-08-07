from warehouse.connection import get_connection


def build():

    conn = get_connection()

    conn.execute(
        "CREATE SCHEMA IF NOT EXISTS gold"
    )

    conn.execute(
        """
        DROP TABLE IF EXISTS gold.daily_revenue
        """
    )

    conn.execute(
        """
        CREATE TABLE gold.daily_revenue AS

        SELECT

            DATE(created_at) AS revenue_date,

            COUNT(*) AS successful_payments,

            SUM(amount) AS revenue

        FROM silver.customer_payments

        WHERE status='SUCCESS'

        GROUP BY 1

        ORDER BY 1
        """
    )

    conn.execute(
        """
        DROP TABLE IF EXISTS gold.executive_dashboard
        """
    )

    conn.execute(
        """
        CREATE TABLE gold.executive_dashboard AS

        SELECT

            COUNT(DISTINCT customer_id) AS customers,

            COUNT(DISTINCT order_id) AS orders,

            SUM(amount) AS revenue,

            AVG(amount) AS average_order_value

        FROM silver.customer_payments

        WHERE status='SUCCESS'
        """
    )

    conn.close()


if __name__ == "__main__":
    build()