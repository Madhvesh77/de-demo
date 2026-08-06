from dataclasses import dataclass


@dataclass
class Customer:

    customer_code: str

    first_name: str

    city: str

    status: str