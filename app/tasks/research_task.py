from crewai import Task

def create_research_task(agent, topic):
    return Task(
        description=f"""
        Research in detail about: {topic}

        Limit response to:
        - 600 words maximum
        - Bullet points where possible
        - No unnecessary elaboration
        """,
        expected_output="Concise structured research summary under 600 words.",
        agent=agent
    )
