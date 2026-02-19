from crewai import Agent
from app.llm.provider import get_llm


def create_writer():

    return Agent(
        role="Senior AI Research Writer",
        goal="""
Produce a technically rigorous, evidence-backed structured report.
All claims must include dataset, metric, numeric value, and baseline comparison.
Avoid vague statements.
""",
        backstory="""
You are a senior AI researcher writing publication-grade reports.
You demand quantitative evidence and precise methodology.
""",
        llm=get_llm("writer"),
        verbose=True
    )
