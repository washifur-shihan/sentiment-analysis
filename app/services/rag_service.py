from app.services.pinecone_service import get_index
from app.services.embedding_service import embed_text
from app.core.config import settings

def retrieve_context(query_text: str, top_k: int = 3) -> list[str]:
    index = get_index()
    query_vector = embed_text(query_text)

    response = index.query(
        namespace=settings.PINECONE_NAMESPACE,
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )

    hits = []
    for match in response["matches"]:
        metadata = match.get("metadata", {})
        text = metadata.get("text")
        if text:
            hits.append(text)

    return hits