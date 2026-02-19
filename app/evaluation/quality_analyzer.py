import re


def count_weaknesses(text: str) -> int:
    """
    Counts real weakness bullet points under the WEAKNESSES section.
    Supports:
    - Dash bullets (- item)
    - Star bullets (* item)
    - Numbered bullets (1. item)
    """

    match = re.search(
        r"WEAKNESSES:(.*?)(IMPROVEMENTS:|$)",
        text,
        re.DOTALL | re.IGNORECASE
    )

    if not match:
        return 0

    section = match.group(1).strip()

    lines = section.split("\n")

    count = 0

    for line in lines:
        line = line.strip()

        # Match bullet patterns only
        if re.match(r"^(-|\*|\d+\.)\s+", line):
            count += 1

    return count
