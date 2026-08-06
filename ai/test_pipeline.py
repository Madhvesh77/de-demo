from ai.planner import create_plan
from ai.sql_generator import generate_sql


question = input("Question : ")

plan = create_plan(question)

print("\n============================")
print("Generated Plan")
print("============================")

print(plan)

sql = generate_sql(plan)

print("\n============================")
print("Generated SQL")
print("============================")

print(sql)