from crewai import LLM


def get_ollama_llm():
    return LLM(
        model="ollama/llama3.1:8b",
        temperature=0.2,
    )
