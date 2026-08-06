import random

ORDER_STATUSES = [
    "PLACED",
    "SHIPPED",
    "DELIVERED",
]

PAYMENT_STATUSES = [
    "SUCCESS",
    "FAILED",
]

PAYMENT_TYPES = [
    "CARD",
    "UPI",
    "NET_BANKING",
]


def generate_order(customer_id):

    return {
        "customer_id": customer_id,
        "status": random.choice(ORDER_STATUSES),
    }


def generate_order_item(order_id, product_id, price):

    quantity = random.randint(1, 3)

    return {
        "order_id": order_id,
        "product_id": product_id,
        "quantity": quantity,
        "amount": round(price * quantity, 2),
    }


def generate_payment(order_id, amount):

    return {
        "order_id": order_id,
        "amount": amount,
        "type": random.choice(PAYMENT_TYPES),
        "status": random.choices(
            PAYMENT_STATUSES,
            weights=[95, 5],
        )[0],
    }