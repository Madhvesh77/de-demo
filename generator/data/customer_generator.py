"""
Generate fake customers and insert them into PostgreSQL.
"""

from faker import Faker
from pathlib import Path
import sys

# Allow importing db.py from parent folder
ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from db import get_connection

fake = Faker()


def generate_customer() -> int:
    """
    Creates one customer and returns its database ID.
    """

    connection = get_connection()
    cursor = connection.cursor()

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
        RETURNING id;
        """,
        (
            fake.unique.bothify(text="CUST-#####"),
            fake.first_name(),
            fake.city(),
            "ACTIVE",
        ),
    )

    customer_id = cursor.fetchone()[0]

    connection.commit()

    cursor.close()
    connection.close()

    return customer_id


if __name__ == "__main__":

    NUMBER_OF_CUSTOMERS = 10

    print(f"Generating {NUMBER_OF_CUSTOMERS} customers...\n")

    for _ in range(NUMBER_OF_CUSTOMERS):
        customer_id = generate_customer()
        print(f"Created customer {customer_id}")

    print("\n✅ Done!")