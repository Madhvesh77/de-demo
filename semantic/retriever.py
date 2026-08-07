from semantic.loader import load_catalog


catalog = load_catalog()


KEYWORDS = {

    "revenue": [
        "payments",
        "orders",
        "order_items",
    ],

    "customer": [
        "customers",
        "orders",
    ],

    "inventory": [
        "inventory",
        "products",
    ],

    "product": [
        "products",
        "order_items",
    ],

    "payment": [
        "payments",
    ],
}


def retrieve(question):

    question = question.lower()

    selected = set()

    for keyword, tables in KEYWORDS.items():

        if keyword in question:

            selected.update(tables)

    context = []

    for table in selected:

        context.append(

            catalog["tables"][table]

        )

    return context