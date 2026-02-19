from crewai import Agent
from app.llm.provider import get_llm


def create_researcher(topic):

    return Agent(
        role="AI Research Analyst",
        goal=f"""
Conduct deep technical research on: {topic}.
All claims must include dataset name, metric, numeric value, and baseline comparison.
Avoid vague statements.
""",
        backstory="""
You are a rigorous AI researcher who values quantitative evidence,
proper methodology, and reproducibility.
""",
        llm=get_llm("researcher"),
        verbose=True
    )
