from pathlib import Path

import duckdb

connection = duckdb.connect(
    "warehouse/warehouse.db"
)

queries = Path(
    "warehouse/queries"
).glob("*.sql")

for query in sorted(queries):

    print()

    print("="*60)

    print(query.stem.upper())

    print("="*60)

    sql = query.read_text()

    print(
        connection.sql(sql).df()
    )