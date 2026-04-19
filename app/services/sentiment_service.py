from app.services.feature_extractor import extract_features
from app.services.rule_engine import apply_rules
from app.services.summarizer import make_summary
from app.services.rag_service import retrieve_context

def analyze_sentiment(text: str) -> dict:
    evidence = retrieve_context(text, top_k=3)

    features = extract_features(text)
    decision = apply_rules(features)
    summary = make_summary(decision["label"], features)

    confidence = decision["confidence"]
    if len(evidence) >= 2:
        confidence = min(0.99, confidence + 0.03)
    elif len(evidence) == 1:
        confidence = min(0.99, confidence + 0.01)

    return {
        "label": decision["label"],
        "confidence": confidence,
        "summary": summary,
        "matched_rules": decision["matched_rules"],
        "evidence": evidence
    }