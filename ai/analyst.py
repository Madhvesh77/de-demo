import ollama

from ai.schema_reader import read_schema


schema = read_schema()

question = input(
    "Ask a business question: "
)

prompt = f"""

You are a SQL analyst.

Database schema:

{schema}

Return ONLY SQL.

Question:

{question}

"""

response = ollama.chat(

    model="llama3.2:3b",

    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ]
)

print()

print(response["message"]["content"])