from crewai import Crew
from app.agents.researcher import create_researcher
from app.agents.verifier import create_verifier
from app.agents.writer import create_writer
from app.agents.critic import create_critic
from app.tasks.research_task import create_research_task
from app.tasks.verification_task import create_verification_task
from app.tasks.writing_task import create_writing_task
from app.tasks.critique_task import create_critique_task


def build_crew(topic: str, feedback_context: str = ""):
    """
    Builds the multi-agent crew.
    If feedback_context is provided, it injects improvement guidance
    into the research phase for iterative optimization.
    """

    # Inject feedback into topic if available
    enhanced_topic = topic
    if feedback_context:
        enhanced_topic = f"""
        ORIGINAL TOPIC:
        {topic}

        IMPROVEMENT INSTRUCTIONS:
        Improve the next output by addressing previous weaknesses
        and applying suggested improvements.

        PREVIOUS FEEDBACK CONTEXT:
        {feedback_context}
        """

    # Create agents
    researcher = create_researcher(enhanced_topic)
    verifier = create_verifier()
    writer = create_writer()
    critic = create_critic()

    # Create tasks
    research_task = create_research_task(researcher, enhanced_topic)
    verification_task = create_verification_task(verifier)
    writing_task = create_writing_task(writer)
    critique_task = create_critique_task(critic)

    # Build crew
    crew = Crew(
        agents=[researcher, verifier, writer, critic],
        tasks=[
            research_task,
            verification_task,
            writing_task,
            critique_task
        ],
        verbose=True
    )

    return crew
