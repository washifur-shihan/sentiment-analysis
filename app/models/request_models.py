from pydantic import BaseModel, Field

class SentimentRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000)
    user_id: str | None = None
    namespace: str | None = "default"
