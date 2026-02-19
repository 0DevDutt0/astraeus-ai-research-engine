from crewai import Agent
from app.llm.provider import get_llm


def create_verifier():

    return Agent(
        role="Fact Verification Specialist",
        goal="""
Strictly verify research findings.
Identify inconsistencies, unsupported claims, and hallucinations.
Require numerical evidence for performance claims.
""",
        backstory="""
You are a skeptical AI auditor who challenges weak assumptions
and enforces methodological rigor.
""",
        llm=get_llm("verifier"),
        verbose=True
    )
