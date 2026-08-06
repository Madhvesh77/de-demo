def save_inventory(cursor, inventory_items):

    for item in inventory_items:

        cursor.execute(
            """
            INSERT INTO inventory
            (
                product_id,
                quantity,
                status
            )
            VALUES
            (
                %s,%s,%s
            )
            """,
            (
                item["product_id"],
                item["quantity"],
                item["status"],
            ),
        )