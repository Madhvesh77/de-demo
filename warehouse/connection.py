import duckdb

DATABASE = "warehouse/warehouse.db"


def get_connection():
    return duckdb.connect(DATABASE)