def create_plan(question):

    question = question.lower()

    if "revenue" in question:

        return {
            "intent": "metric_lookup",
            "metric": "Revenue",
            "entities": [
                "payments"
            ]
        }

    if "customer" in question:

        return {
            "intent": "ranking",
            "metric": "Customer Lifetime Value",
            "entities": [
                "orders"
            ]
        }

    raise Exception(
        "Unknown question"
    )