import json
import os
import pandas as pd

PATH = "metrics/metrics.json"

def load_metrics():
    if not os.path.exists(PATH):
        return pd.DataFrame()
    with open(PATH, "r") as f:
        return pd.DataFrame(json.load(f))

def compute_statistics(df):
    if df.empty:
        return {}

    return {
        "average_score": df["score"].mean(),
        "average_iterations": df["iterations"].mean(),
        "total_runs": len(df),
        "failure_rate": len(df[df["score"] < 8]) / len(df)
    }
