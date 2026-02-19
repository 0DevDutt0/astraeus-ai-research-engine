import json
import os
from datetime import datetime

PATH = "metrics/metrics.json"
os.makedirs("metrics", exist_ok=True)

def save_metrics(topic, score, iterations):

    data = {
        "timestamp": datetime.now().isoformat(),
        "topic": topic,
        "score": score,
        "iterations": iterations
    }

    if os.path.exists(PATH):
        with open(PATH, "r") as f:
            metrics = json.load(f)
    else:
        metrics = []

    metrics.append(data)

    with open(PATH, "w") as f:
        json.dump(metrics, f, indent=4)
