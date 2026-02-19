import re


def extract_score(text: str) -> float:
    """
    Extracts numeric score from formats like:
    SCORE: 8
    SCORE: 8/10
    ### SCORE: 8/10
    """

    match = re.search(r"SCORE:\s*(\d+(\.\d+)?)(?:\s*/\s*10)?", text, re.IGNORECASE)

    if match:
        return float(match.group(1))

    return 0.0
