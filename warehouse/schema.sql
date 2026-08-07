CREATE TABLE IF NOT EXISTS etl_metadata
(
    table_name VARCHAR PRIMARY KEY,

    last_loaded_at TIMESTAMP,

    last_loaded_id BIGINT,

    last_run_status VARCHAR,

    rows_loaded BIGINT,

    run_duration_seconds DOUBLE
);

CREATE SCHEMA IF NOT EXISTS bronze;

CREATE SCHEMA IF NOT EXISTS silver;

CREATE SCHEMA IF NOT EXISTS gold;