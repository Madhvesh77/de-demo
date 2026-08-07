from semantic.retriever import retrieve


def explain(question: str):

    context = retrieve(question)

    print("\n" + "=" * 60)
    print("🧠 AI Reasoning")
    print("=" * 60)

    print("\nQuestion")
    print("----------------------------------------")
    print(question)

    print("\nBusiness Context")
    print("----------------------------------------")

    for item in context:

        print(f"Description : {item.get('description','')}")

        if "business_rules" in item:

            for rule in item["business_rules"]:

                print(f"✓ {rule}")

    print()

    return context