import ollama

from ai.schema_reader import read_schema

from semantic.retriever import retrieve


schema = read_schema()

question = input(
    "Ask a business question: "
)

semantic_context = retrieve(question)


prompt = f"""

You are an expert SQL analyst.

Relevant Business Context

{semantic_context}

Database Schema

{schema}

Return ONLY executable DuckDB SQL.

Question:

{question}

"""
print("\n========== PROMPT ==========\n")
print(prompt)
print("\n============================\n")

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