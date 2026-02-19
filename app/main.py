import time
from litellm.exceptions import RateLimitError

from app.crew.crew_builder import build_crew
from app.evaluation.score_parser import extract_score
from app.evaluation.metrics_store import save_metrics
from app.memory.memory_manager import save_run_output
from app.evaluation.feedback_parser import extract_feedback_sections
from app.evaluation.quality_analyzer import count_weaknesses


THRESHOLD = 8
MAX_ITER = 3
PLATEAU_DELTA = 0.3


def run():
    topic = input("Enter topic: ")

    iteration = 0
    final_output = None
    feedback_context = ""
    score_history = []

    while iteration < MAX_ITER:
        print(f"\nIteration {iteration + 1}...\n")

        try:
            crew = build_crew(topic, feedback_context)
            result = crew.kickoff()

        except RateLimitError:
            print("Rate limit reached. Retrying in 12 seconds...")
            time.sleep(12)
            continue

        result_text = str(result)

        score = extract_score(result_text)
        weaknesses_count = count_weaknesses(result_text)

        score_history.append(score)

        print(f"Score Received: {score}")
        print(f"Weakness Count: {weaknesses_count}\n")

        # Condition 1: Quality threshold met
        if score >= THRESHOLD:
            print("Quality threshold reached.\n")
            final_output = result_text
            break

        # Condition 2: High-quality plateau detection
        if len(score_history) >= 2:
            score_change = abs(score_history[-1] - score_history[-2])

            if (
                score >= 7.5
                and weaknesses_count <= 3
                and score_change < PLATEAU_DELTA
            ):
                print("High-quality plateau detected. Accepting output.\n")
                final_output = result_text
                break

        # Prepare feedback for next iteration
        feedback_context = extract_feedback_sections(result_text)
        iteration += 1

    # Final handling
    if final_output:
        save_metrics(topic, score_history[-1], iteration + 1)
        save_run_output(topic, final_output)
        print(final_output)
    else:
        print("Failed to reach quality threshold within max iterations.")


if __name__ == "__main__":
    run()
