import random


def generate_inventory(product_id):

    return {
        "product_id": product_id,
        "quantity": random.randint(20, 250),
        "status": "IN_STOCK",
    }