

from pydantic import BaseModel
from typing import List

class SentimentResponse(BaseModel):
    label: str
    confidence: float
    summary: str
    matched_rules: List[str]
    evidence: List[str]