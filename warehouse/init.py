from pathlib import Path

from warehouse.connection import get_connection


def initialize():

    connection = get_connection()

    schema = Path("warehouse/schema.sql").read_text()

    connection.execute(schema)

    connection.close()


if __name__ == "__main__":
    initialize()