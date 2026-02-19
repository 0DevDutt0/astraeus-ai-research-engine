import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt

st.title("🚀 Astraeus AI Observability Dashboard")

with open("data/metrics.json", "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)

st.metric("Total Runs", len(df))
st.metric("Average Score", round(df["score"].mean(), 2))
st.metric("Average Latency (s)", round(df["latency_seconds"].mean(), 2))

st.subheader("Score Over Time")
plt.figure()
plt.plot(df["score"])
plt.xlabel("Run")
plt.ylabel("Score")
st.pyplot(plt)

st.subheader("Latency Over Time")
plt.figure()
plt.plot(df["latency_seconds"])
plt.xlabel("Run")
plt.ylabel("Seconds")
st.pyplot(plt)
