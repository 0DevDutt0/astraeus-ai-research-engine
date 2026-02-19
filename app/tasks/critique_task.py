from crewai import Task

def create_critique_task(agent):
    return Task(
        description="""
        Evaluate the report concisely.

        Format strictly:

        SCORE: <1-10>
        STRENGTHS: (max 5 bullet points)
        WEAKNESSES: (max 5 bullet points)
        IMPROVEMENTS: (max 5 bullet points)

        Keep total response under 400 words.
        """,
        expected_output="Structured evaluation under 400 words.",
        agent=agent
    )
