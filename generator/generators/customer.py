from faker import Faker

from generator.models.customer import Customer

fake = Faker()


def generate_customer():

    return Customer(
        customer_code=fake.unique.bothify("CUST-#####"),
        first_name=fake.first_name(),
        city=fake.city(),
        status="ACTIVE",
    )


if __name__ == "__main__":

    customer = generate_customer()

    print(customer)