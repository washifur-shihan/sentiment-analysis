from pinecone import Pinecone
from app.core.config import settings

pc = Pinecone(api_key=settings.PINECONE_API_KEY)

def get_index():
    return pc.Index(settings.PINECONE_INDEX_NAME)
