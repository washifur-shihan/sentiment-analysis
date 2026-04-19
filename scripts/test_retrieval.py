from app.services.rag_service import retrieve_context

query = "I am frustrated because this service is broken and I need it fixed ASAP"

results = retrieve_context(query, top_k=3)

print("Retrieved evidence:")
for i, item in enumerate(results, start=1):
    print(f"{i}. {item}")