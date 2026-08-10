from llm import create_plan


question = "Why does Swift 6 require Sendable?"

plan = create_plan(question)

print("Summary:")
print(plan.summary)

print("\nSearch queries:")

for query in plan.search_queries:
    print(f"- {query}")

print("\nPriority:")
print(plan.priority.value)

print("\nRequires code changes:")
print(plan.requires_code_changes)