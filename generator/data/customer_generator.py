"""
Customer Generator
"""

from faker import Faker

from generator.database import database_session

fake = Faker()


def generate_customer(cursor):

    cursor.execute(
        """
        INSERT INTO customers
        (
            customer_code,
            first_name,
            city,
            status,
            created_at,
            updated_at
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            NOW(),
            NOW()
        )
        RETURNING id
        """,
        (
            fake.unique.bothify("CUST-#####"),
            fake.first_name(),
            fake.city(),
            "ACTIVE",
        ),
    )

    return cursor.fetchone()[0]


def generate_customers(number_of_customers: int):

    created = []

    with database_session() as cursor:

        for _ in range(number_of_customers):

            customer_id = generate_customer(cursor)

            created.append(customer_id)

    return created


if __name__ == "__main__":

    NUMBER_OF_CUSTOMERS = 20

    print(f"Generating {NUMBER_OF_CUSTOMERS} customers...")

    customer_ids = generate_customers(NUMBER_OF_CUSTOMERS)

    print()

    print(f"Created {len(customer_ids)} customers.")

    print(f"First Customer ID : {customer_ids[0]}")

    print(f"Last Customer ID  : {customer_ids[-1]}")