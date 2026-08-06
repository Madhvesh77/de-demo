"""
Transaction helper.

Creates a single database transaction that can be
shared across repositories.
"""

from contextlib import contextmanager

from generator.connection import get_connection


@contextmanager
def transaction():

    connection = get_connection()
    cursor = connection.cursor()

    try:

        yield cursor

        connection.commit()

    except Exception:

        connection.rollback()

        raise

    finally:

        cursor.close()
        connection.close()