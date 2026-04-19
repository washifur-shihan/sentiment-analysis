import json
from app.services.pinecone_service import get_index
from app.services.embedding_service import embed_text
from app.core.config import settings

def ingest():
    index = get_index()

    with open("app/data/kb_seed.json", "r", encoding="utf-8") as f:
        records = json.load(f)

    vectors = []
    for item in records:
        vectors.append({
            "id": item["id"],
            "values": embed_text(item["text"]),
            "metadata": {
                "text": item["text"],
                "category": item["category"]
            }
        })

    index.upsert(vectors=vectors, namespace=settings.PINECONE_NAMESPACE)
    print("Knowledge base ingested successfully.")

if __name__ == "__main__":
    ingest()