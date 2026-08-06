from generator.generators.customer import generate_customer
from generator.repositories.customer_repository import save


customer = generate_customer()

customer_id = save(customer)

print(customer)

print()

print(f"Saved with ID {customer_id}")