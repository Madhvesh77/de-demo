import duckdb


def read_schema():

    conn = duckdb.connect(
        "warehouse/warehouse.db"
    )

    schema = []

    tables = conn.sql(
        "SHOW TABLES"
    ).fetchall()

    for table in tables:

        table = table[0]

        columns = conn.sql(
            f"DESCRIBE {table}"
        ).fetchall()

        schema.append(
            {
                "table": table,
                "columns": columns,
            }
        )

    return schema