from app.memory.memory_store import store_memory, retrieve_memory

def save_run_output(topic, output):
    text = f"TOPIC: {topic}\nOUTPUT:\n{output}"
    store_memory(text)

def get_relevant_past_memory(topic):
    return retrieve_memory(topic)
