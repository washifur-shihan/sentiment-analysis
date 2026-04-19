
def make_summary(label: str, features: dict) -> str:
    if label == "urgent":
        return "The text expresses urgency with negative pressure or an immediate action request."
    if label == "frustrated":
        return "The text shows dissatisfaction and a complaint-oriented tone."
    if label == "negative":
        return "The text carries a negative tone."
    if label == "positive":
        return "The text carries a positive and supportive tone."
    if label == "mixed":
        return "The text contains both positive and negative emotional signals."
    return "The text appears emotionally balanced or neutral."