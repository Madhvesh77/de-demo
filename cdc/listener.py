import psycopg

connection = psycopg.connect(
    host="localhost",
    dbname="shopsmart",
    user="admin",
    password="shopsmart123",
)

connection.autocommit = True

connection.execute(
    "LISTEN payments_channel;"
)

print("Listening...")

while True:

    connection.poll()

    while connection.notifies:

        notify = connection.notifies.pop()

        print(
            f"Payment inserted: {notify.payload}"
        )