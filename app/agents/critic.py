from crewai import Agent
from app.llm.provider import get_llm

def create_critic():
    return Agent(
        role="AI Output Critic",
        goal="Critically evaluate technical reports and assign quality scores.",
        backstory="Senior AI systems evaluator focused on rigor and clarity.",
        llm=get_llm("critic"),
        verbose=True
    )
