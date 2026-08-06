from generator.generators.customer import generate_customer
from generator.generators.product import (
    generate_categories,
    generate_product,
)

from generator.repositories.customer_repository import save
from generator.repositories.product_repository import (
    save_categories,
    save_products,
)


def seed_database():

    print("\nGenerating Categories...")

    categories = generate_categories()

    category_ids = save_categories(categories)

    print(f"Created {len(category_ids)} categories.")

    print("\nGenerating Products...")

    products = []

    for category_id in category_ids:

        for _ in range(10):

            products.append(
                generate_product(category_id)
            )

    save_products(products)

    print(f"Created {len(products)} products.")

    print("\nGenerating Customers...")

    for _ in range(10):

        save(generate_customer())

    print("Created 10 customers.")

    print("\n✅ Seed completed.\n")