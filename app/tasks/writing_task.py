from crewai import Task

def create_writing_task(agent):

    return Task(
        description="""
Generate a structured technical research report.

Mandatory Requirements:

1. Every performance claim must include:
   - Dataset name
   - Metric (Accuracy, AUC, F1, Sensitivity, etc.)
   - Numeric value
   - CNN baseline comparison

2. Include a comparison table in plain text format.

3. Include explicit limitations section.

4. Include implementation details:
   - Model variant (ViT-B/16, Swin-B, DeiT, etc.)
   - Optimizer
   - Learning rate
   - Epoch count

5. No vague language:
   - Do NOT use "promising"
   - Do NOT use "state-of-the-art" without numeric comparison
   - Do NOT exaggerate

6. Must include:
   - Datasets (e.g., EyePACS, APTOS, REFUGE)
   - CNN baseline (ResNet50 or EfficientNet)

Word limit: 800 words.
""",
        agent=agent,
        expected_output="A rigorous technical research-style report with quantitative comparisons."
    )
