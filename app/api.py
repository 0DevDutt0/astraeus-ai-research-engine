from fastapi import FastAPI
from pydantic import BaseModel
from app.crew.crew_builder import build_crew
from app.evaluation.score_parser import extract_score
from app.evaluation.quality_analyzer import count_weaknesses

app = FastAPI()


class TopicRequest(BaseModel):
    topic: str


@app.post("/analyze")
def analyze(request: TopicRequest):

    crew = build_crew(request.topic)
    result = crew.kickoff()

    result_text = str(result)

    score = extract_score(result_text)
    weakness_count = count_weaknesses(result_text)

    return {
        "topic": request.topic,
        "score": score,
        "weakness_count": weakness_count,
        "output": result_text
    }
