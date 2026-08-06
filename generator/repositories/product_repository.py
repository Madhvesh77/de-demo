from generator.connection import get_connection


def save_categories(categories):

    conn = get_connection()
    cur = conn.cursor()

    ids = []

    for category in categories:

        cur.execute(
            """
            INSERT INTO categories(name, status)
            VALUES(%s,%s)
            RETURNING id;
            """,
            (
                category,
                "ACTIVE",
            ),
        )

        ids.append(cur.fetchone()[0])

    conn.commit()

    cur.close()
    conn.close()

    return ids


def save_products(products):

    conn = get_connection()
    cur = conn.cursor()

    for product in products:

        cur.execute(
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

    conn.commit()

    cur.close()
    conn.close()