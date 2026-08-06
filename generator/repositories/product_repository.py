def save_categories(cursor, categories):

    ids = []

    for category in categories:

        cursor.execute(
            """
            INSERT INTO categories
            (
                name,
                status
            )
            VALUES
            (
                %s,%s
            )
            RETURNING id
            """,
            (
                category,
                "ACTIVE",
            ),
        )

        ids.append(cursor.fetchone()[0])

    return ids


def save_products(cursor, products):

    for product in products:

        cursor.execute(
            """
            INSERT INTO products
            (
                sku,
                category_id,
                name,
                price,
                status
            )
            VALUES
            (
                %s,%s,%s,%s,%s
            )
            """,
            (
                product["sku"],
                product["category_id"],
                product["name"],
                product["price"],
                product["status"],
            ),
        )