def save_order(cursor, order):

    cursor.execute(
        """
        INSERT INTO orders
        (
            customer_id,
            amount,
            status
        )
        VALUES
        (
            %s,
            0,
            %s
        )
        RETURNING id
        """,
        (
            order["customer_id"],
            order["status"],
        ),
    )

    return cursor.fetchone()[0]


def save_order_item(cursor, item):

    cursor.execute(
        """
        INSERT INTO order_items
        (
            order_id,
            product_id,
            quantity,
            amount
        )
        VALUES
        (
            %s,%s,%s,%s
        )
        """,
        (
            item["order_id"],
            item["product_id"],
            item["quantity"],
            item["amount"],
        ),
    )


def update_order_amount(cursor, order_id, amount):

    cursor.execute(
        """
        UPDATE orders
        SET amount=%s
        WHERE id=%s
        """,
        (
            amount,
            order_id,
        ),
    )


def reduce_inventory(cursor, product_id, quantity):

    cursor.execute(
        """
        UPDATE inventory
        SET quantity = quantity - %s,
            updated_at = CURRENT_TIMESTAMP
        WHERE product_id = %s
        """,
        (
            quantity,
            product_id,
        ),
    )


def save_payment(cursor, payment):

    cursor.execute(
        """
        INSERT INTO payments
        (
            order_id,
            amount,
            type,
            status
        )
        VALUES
        (
            %s,%s,%s,%s
        )
        """,
        (
            payment["order_id"],
            payment["amount"],
            payment["type"],
            payment["status"],
        ),
    )