import re

NEGATIVE_WORDS = {
    "bad", "terrible", "awful", "hate", "angry", "upset", "frustrated",
    "disappointed", "useless", "worst", "annoying", "broken"
}
POSITIVE_WORDS = {
    "good", "great", "excellent", "love", "amazing", "happy", "thanks",
    "appreciate", "awesome", "helpful", "perfect"
}
URGENT_WORDS = {
    "urgent", "immediately", "asap", "now", "critical", "emergency"
}

def extract_features(text: str) -> dict:
    lowered = text.lower()
    words = re.findall(r"\b\w+\b", lowered)

    return {
        "text": text,
        "lowered": lowered,
        "word_count": len(words),
        "negative_hits": [w for w in words if w in NEGATIVE_WORDS],
        "positive_hits": [w for w in words if w in POSITIVE_WORDS],
        "urgent_hits": [w for w in words if w in URGENT_WORDS],
        "has_exclamation": "!" in text,
        "has_all_caps_word": any(token.isupper() and len(token) > 2 for token in text.split()),
        "has_question": "?" in text,
    }
