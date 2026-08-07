import psycopg

from cdc.sync import sync_payment

conn = psycopg.connect(
    host="localhost",
    dbname="shopsmart",
    user="admin",
    password="shopsmart123",
    autocommit=True,
)

conn.execute("LISTEN payments_channel;")

print("Listening on payments_channel...")

for notify in conn.notifies():

    payment_id = int(notify.payload)

    print(f"Received payment {payment_id}")

    sync_payment(payment_id)