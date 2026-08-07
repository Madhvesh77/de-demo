def generate_sql(plan, metric):

    if "sql" in metric:
        sql = metric["sql"]

        table = sql["table"]

        aggregation = sql["aggregation"]

        filters = metric.get("filters", {})

        where_clause = ""

        if filters:

            conditions = [
                f"{column}='{value}'"
                for column, value in filters.items()
            ]

            where_clause = " WHERE " + " AND ".join(conditions)

        return f"""
SELECT
    {aggregation} AS value
FROM {table}
{where_clause};
"""
