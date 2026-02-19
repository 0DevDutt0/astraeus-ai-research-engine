from crewai import Task

def create_verification_task(agent):
    return Task(
        description="""
        Verify research findings.

        Return:
        - Confirmed facts (max 8 points)
        - Inconsistencies (max 5 points)
        - Possible hallucinations (max 3 points)

        Be concise.
        """,
        expected_output="Compact verification report.",
        agent=agent
    )
