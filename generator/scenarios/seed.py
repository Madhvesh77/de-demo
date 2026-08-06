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
from generator.generators.inventory import generate_inventory
from generator.repositories.inventory_repository import save_inventory
from generator.generators.order import (
    generate_order,
    generate_order_item,
    generate_payment,
)

from generator.repositories.order_repository import (
    save_order,
    save_order_item,
    update_order_amount,
    reduce_inventory,
    save_payment,
)
from generator.transaction import transaction


def seed_database():

    with transaction() as cursor:
        cursor.execute("TRUNCATE TABLE customer_campaigns RESTART IDENTITY CASCADE;")
        cursor.execute("TRUNCATE TABLE marketing_campaigns RESTART IDENTITY CASCADE;")
        cursor.execute("TRUNCATE TABLE returns RESTART IDENTITY CASCADE;")
        cursor.execute("TRUNCATE TABLE payments RESTART IDENTITY CASCADE;")
        cursor.execute("TRUNCATE TABLE order_items RESTART IDENTITY CASCADE;")
        cursor.execute("TRUNCATE TABLE orders RESTART IDENTITY CASCADE;")
        cursor.execute("TRUNCATE TABLE inventory RESTART IDENTITY CASCADE;")
        cursor.execute("TRUNCATE TABLE products RESTART IDENTITY CASCADE;")
        cursor.execute("TRUNCATE TABLE categories RESTART IDENTITY CASCADE;")
        cursor.execute("TRUNCATE TABLE customers RESTART IDENTITY CASCADE;")

        print("\nGenerating Categories...")

        categories = generate_categories()

        category_ids = save_categories(
            cursor,
            categories,
        )

        print(f"Created {len(category_ids)} categories.")

        products = []

        print("\nGenerating Products...")

        for category_id in category_ids:

            for _ in range(10):

                products.append(
                    generate_product(category_id)
                )

        save_products(
            cursor,
            products,
        )

        print(f"Created {len(products)} products.")

        print("\nGenerating Inventory...")

        inventory = []

        for product_id in range(1, len(products) + 1):

            inventory.append(
                generate_inventory(product_id)
            )

        save_inventory(
            cursor,
            inventory,
        )

        print(f"Created {len(inventory)} inventory records.")

        print("\nGenerating Customers...")

        for _ in range(10):

            save(
                cursor,
                generate_customer(),
            )

        print("Created 10 customers.")

        from generator.generators.order import (
            generate_order,
            generate_order_item,
        )

        from generator.repositories.order_repository import (
            save_order,
            save_order_item,
            update_order_amount,
            reduce_inventory,
        )

        from generator.repositories.payment_repository import (
            create_payment,
        )

        print("\nGenerating Orders...")

        for customer_id in range(1, 11):

            order = generate_order(customer_id)

            order_id = save_order(cursor, order)

            product_id = customer_id

            cursor.execute(
                """
                SELECT price
                FROM products
                WHERE id=%s
                """,
                (product_id,),
            )

            price = float(cursor.fetchone()[0])

            item = generate_order_item(
                order_id,
                product_id,
                price,
            )

            save_order_item(
                cursor,
                item,
            )

            update_order_amount(
                cursor,
                order_id,
                item["amount"],
            )

            reduce_inventory(
                cursor,
                product_id,
                item["quantity"],
            )

            payment = generate_payment(
                order_id,
                item["amount"],
            )

            save_payment(
                cursor,
                payment,
            )

        print("Created 10 orders.")
    print("\n✅ Seed completed.")