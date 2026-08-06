from generator.connection import get_connection
from generator.models.customer import Customer


def save(customer: Customer) -> int:

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO customers
        (
            customer_code,
            first_name,
            city,
            status
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s
        )
        RETURNING id;
        """,
        (
            customer.customer_code,
            customer.first_name,
            customer.city,
            customer.status,
        ),
    )

    customer_id = cursor.fetchone()[0]

    connection.commit()

    cursor.close()

    connection.close()

    return customer_id