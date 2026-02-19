from crewai import LLM


def route_model(role=None):

    # Heavy reasoning agent
    if role == "researcher":
        return LLM(
            model="ollama/deepseek-r1:32b",
            temperature=0.2,
        )

    # Strict evaluator
    if role == "critic":
        return LLM(
            model="ollama/llama3.1:8b",
            temperature=0.1,
        )

    # Verification reasoning
    if role == "verifier":
        return LLM(
            model="ollama/llama3.1:8b",
            temperature=0.2,
        )

    # Default (writer)
    return LLM(
        model="ollama/llama3.1:8b",
        temperature=0.3,
    )
