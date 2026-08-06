"""
Database helper.

Provides a reusable database session that automatically
opens and closes PostgreSQL connections.
"""

from contextlib import contextmanager

from generator.connection import get_connection

@contextmanager
def database_session():
    """
    Creates a PostgreSQL session.

    Automatically commits if everything succeeds.

    Rolls back if something fails.

    Closes everything afterwards.
    """

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