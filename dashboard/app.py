import streamlit as st
import requests
import time
import json
import random
from datetime import datetime

st.set_page_config(
    page_title="Astraeus AI Research Engine",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

body {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

.hero {
    padding: 60px 20px;
    text-align: center;
    background: linear-gradient(270deg, #4f46e5, #7c3aed, #4f46e5);
    background-size: 400% 400%;
    animation: gradientShift 10s ease infinite;
    border-radius: 20px;
    margin-bottom: 40px;
}

@keyframes gradientShift {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.card {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(15px);
    padding: 20px;
    border-radius: 16px;
    margin-bottom: 20px;
}

.strength { border-left: 5px solid #10b981; }
.weakness { border-left: 5px solid #f59e0b; }
.improve { border-left: 5px solid #3b82f6; }

.footer {
    text-align: center;
    margin-top: 60px;
    opacity: 0.6;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>Astraeus AI Research Engine</h1>
<p>Autonomous Multi-Agent Research & Evaluation Platform</p>
</div>
""", unsafe_allow_html=True)

topic = st.text_input(
    "Enter Research Topic",
    placeholder="Vision Transformers for Retinal Disease Detection"
)

run = st.button("Run Analysis")

quotes = [
    "Analyzing multi-agent outputs...",
    "Optimizing research quality...",
    "Applying verification protocols...",
    "Evaluating technical rigor..."
]

if run:
    if not topic.strip():
        st.warning("Please enter a research topic.")
        st.stop()

    try:
        with st.spinner(random.choice(quotes)):
            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                json={"topic": topic},
                timeout=300
            )
            response.raise_for_status()
            data = response.json()
            time.sleep(0.5)

        st.session_state["score"] = data.get("score", 0.0)
        st.session_state["weaknesses"] = data.get("weakness_count", 0)
        st.session_state["output"] = data.get("output", "")

    except Exception as e:
        st.error(f"API Error: {str(e)}")
        st.stop()

if "output" not in st.session_state:
    st.stop()

score = st.session_state["score"]
weaknesses = st.session_state["weaknesses"]
output = st.session_state["output"]

st.markdown("## Evaluation Metrics")

col1, col2 = st.columns(2)

with col1:
    if score >= 8:
        status_color = "green"
        status_text = "High Quality"
    elif score >= 6:
        status_color = "orange"
        status_text = "Moderate Quality"
    else:
        status_color = "red"
        status_text = "Needs Improvement"

    st.metric("Quality Score", score)
    st.markdown(
        f"<span style='color:{status_color}; font-weight:600;'>Status: {status_text}</span>",
        unsafe_allow_html=True
    )

with col2:
    st.metric("Weakness Count", weaknesses)

strengths = []
weak = []
improve = []

current_section = None

for raw_line in output.split("\n"):
    line = raw_line.strip()

    if not line:
        continue

    upper = line.upper()

    if "STRENGTHS" in upper:
        current_section = "s"
        continue

    if "WEAKNESSES" in upper:
        current_section = "w"
        continue

    if "IMPROVEMENTS" in upper:
        current_section = "i"
        continue

    if current_section == "s":
        strengths.append(line)

    elif current_section == "w":
        weak.append(line)

    elif current_section == "i":
        improve.append(line)

st.markdown("## Research Evaluation Report")

with st.expander("Strengths", expanded=True):
    st.markdown('<div class="card strength">', unsafe_allow_html=True)
    if strengths:
        for s in strengths:
            st.markdown(f"- {s}")
    else:
        st.markdown("No strengths identified.")
    st.markdown('</div>', unsafe_allow_html=True)

with st.expander("Weaknesses"):
    st.markdown('<div class="card weakness">', unsafe_allow_html=True)
    if weak:
        for w in weak:
            st.markdown(f"- {w}")
    else:
        st.markdown("No weaknesses identified.")
    st.markdown('</div>', unsafe_allow_html=True)

with st.expander("Improvements"):
    st.markdown('<div class="card improve">', unsafe_allow_html=True)
    if improve:
        for i in improve:
            st.markdown(f"- {i}")
    else:
        st.markdown("No improvements suggested.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("### Export Options")

colA, colB = st.columns(2)

with colA:
    st.download_button(
        label="Download as Markdown",
        data=output,
        file_name="research_report.md"
    )

with colB:
    st.download_button(
        label="Download as JSON",
        data=json.dumps({
            "score": score,
            "weakness_count": weaknesses,
            "output": output
        }, indent=4),
        file_name="research_report.json"
    )

st.markdown(f"""
<div class="footer">
© {datetime.now().year} Astraeus AI | Version 1.0.0<br>
Built with Streamlit
</div>
""", unsafe_allow_html=True)
