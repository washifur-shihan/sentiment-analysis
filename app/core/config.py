import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "")
    PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "sentiment-agent-index")
    PINECONE_NAMESPACE = os.getenv("PINECONE_NAMESPACE", "sentiment-rules")

settings = Settings()
