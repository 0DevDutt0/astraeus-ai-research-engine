from crewai import LLM

def get_local_llm():
    return LLM(
        model="ollama/llama3.1:8b",
        base_url="http://localhost:11434",
        temperature=0.2,
        max_tokens=1000
    )
