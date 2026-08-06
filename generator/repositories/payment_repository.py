import random


PAYMENT_TYPES = [
    "CARD",
    "UPI",
    "NET_BANKING",
]


def create_payment(cursor, order_id, amount):

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
            order_id,
            amount,
            random.choice(PAYMENT_TYPES),
            "SUCCESS",
        ),
    )