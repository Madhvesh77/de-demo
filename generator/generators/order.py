import random


ORDER_STATUS = [
    "PLACED",
    "SHIPPED",
    "DELIVERED",
]


def generate_order(customer_id):

    return {
        "customer_id": customer_id,
        "status": random.choice(ORDER_STATUS),
    }


def generate_order_item(order_id, product_id, price):

    quantity = random.randint(1, 3)

    return {
        "order_id": order_id,
        "product_id": product_id,
        "quantity": quantity,
        "amount": quantity * price,
    }