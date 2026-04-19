def apply_rules(features: dict) -> dict:
    matched_rules = []

    neg_count = len(features["negative_hits"])
    pos_count = len(features["positive_hits"])
    urgent_count = len(features["urgent_hits"])

    if urgent_count > 0:
        matched_rules.append("urgent_keywords")

    if neg_count >= 2:
        matched_rules.append("strong_negative_words")

    if pos_count >= 2:
        matched_rules.append("strong_positive_words")

    if features["has_all_caps_word"]:
        matched_rules.append("all_caps_emphasis")

    if features["has_exclamation"]:
        matched_rules.append("exclamation_emphasis")

    if urgent_count > 0 and neg_count > 0:
        return {
            "label": "urgent",
            "confidence": 0.95,
            "matched_rules": matched_rules
        }

    if neg_count > 0 and pos_count > 0:
        return {
            "label": "mixed",
            "confidence": 0.82,
            "matched_rules": matched_rules
        }

    if neg_count >= 2:
        return {
            "label": "frustrated",
            "confidence": 0.90,
            "matched_rules": matched_rules
        }

    if neg_count == 1:
        return {
            "label": "negative",
            "confidence": 0.76,
            "matched_rules": matched_rules
        }

    if pos_count >= 2:
        return {
            "label": "positive",
            "confidence": 0.91,
            "matched_rules": matched_rules
        }

    if pos_count == 1:
        return {
            "label": "positive",
            "confidence": 0.72,
            "matched_rules": matched_rules
        }

    return {
        "label": "neutral",
        "confidence": 0.65,
        "matched_rules": matched_rules
    }
