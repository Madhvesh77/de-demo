def main():
        
    import duckdb

    from ai.planner import create_plan
    from ai.knowledge_engine import (
        get_metric,
    )
    from ai.sql_generator import (
        generate_sql,
    )

    db = duckdb.connect(
        "warehouse/warehouse.db"
    )

    print("=" * 60)
    print("🤖 AI DATA ANALYST")
    print("=" * 60)

    question = input("\nQuestion : ")

    plan = create_plan(question)

    metric = get_metric(plan["metric"])

    print("\nBusiness Understanding")
    print("-" * 40)

    print("Metric")

    print(metric["name"])

    print()

    print("Definition")

    print(metric.get("description", "No description available."))

    print()

    print("\nBusiness Rules")
    print("-" * 40)

    if "business_rules" in metric:

        for rule in metric["business_rules"]:

            print(f"✓ {rule}")

    elif "filters" in metric:

        print("Filters")

        for key, value in metric["filters"].items():

            print(f"✓ {key} = {value}")

    else:

        print("No business rules available.")

    sql = generate_sql(
        plan,
        metric,
    )

    print("\nGenerated SQL")
    print("-" * 40)

    print(sql)

    result = db.sql(sql).df()

    print("\nResult")
    print("-" * 40)

    print(result)

    print("\nBusiness Summary")
    print("-" * 40)

    if plan["metric"] == "Revenue":

        revenue = result.iloc[0, 0]

        print(

            f"Today's successful revenue is ₹{revenue:,.2f}"

        )

    elif plan["metric"] == "Customer Lifetime Value":

        print(

            "These are the highest value customers."

        )

if __name__ == "__main__":
    main()
