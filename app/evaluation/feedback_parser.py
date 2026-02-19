import re

def extract_feedback_sections(text: str) -> str:
    """
    Extract WEAKNESSES and IMPROVEMENTS sections only.
    Returns compressed improvement instructions.
    """

    weaknesses = ""
    improvements = ""

    weak_match = re.search(r"WEAKNESSES:(.*?)(IMPROVEMENTS:|$)", text, re.DOTALL)
    if weak_match:
        weaknesses = weak_match.group(1).strip()

    improve_match = re.search(r"IMPROVEMENTS:(.*)", text, re.DOTALL)
    if improve_match:
        improvements = improve_match.group(1).strip()

    return f"""
    ADDRESS THESE WEAKNESSES:
    {weaknesses}

    APPLY THESE IMPROVEMENTS:
    {improvements}
    """
