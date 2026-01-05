def calculate_score(title, length):
    score = 0

    # Title clarity
    if len(title) >= 40:
        score += 30
    elif len(title) >= 20:
        score += 20

    # Video length (mid-roll ads)
    if 8 <= length <= 15:
        score += 40
    elif length > 15:
        score += 30

    # Monetization keywords
    keywords = ["how", "review", "best", "tutorial", "guide", "income", "AI", "passive"]
    if any(word in title.lower() for word in keywords):
        score += 30

    return score

