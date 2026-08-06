from generator.models.customer import Customer


def save(cursor, customer: Customer):

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
            %s,%s,%s,%s
        )
        RETURNING id
        """,
        (
            customer.customer_code,
            customer.first_name,
            customer.city,
            customer.status,
        ),
    )

    return cursor.fetchone()[0]