from faker import Faker
import random

fake = Faker()

CATEGORIES = [
    "Electronics",
    "Fashion",
    "Home",
    "Books",
    "Sports",
    "Beauty",
]


def generate_categories():
    return CATEGORIES


def generate_product(category_id):

    adjective = fake.word().capitalize()

    noun = fake.word().capitalize()

    return {
        "sku": fake.unique.bothify("SKU-#####"),
        "category_id": category_id,
        "name": f"{adjective} {noun}",
        "price": round(random.uniform(100, 5000), 2),
        "status": "ACTIVE",
    }