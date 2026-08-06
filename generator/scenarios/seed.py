from generator.generators.customer import generate_customer
from generator.repositories.customer_repository import save


def seed_database(number_of_customers: int = 10):
    """
    Populate the OLTP database with initial data.
    """

    print(f"\nGenerating {number_of_customers} customers...\n")

    for _ in range(number_of_customers):
        customer = generate_customer()
        save(customer)

    print("✅ Initial seed completed.\n")