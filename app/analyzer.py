import anthropic
import os
from app.prompts import SYSTEM_PROMPT

client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

def analyze(metrics):

    prompt = f"""
    {SYSTEM_PROMPT}

    SQL Server Metrics:
    {metrics}

    Tasks:
    1. Identify issue
    2. Suggest fix
    3. Severity (Low/Medium/High)
    4. Root cause
    """

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text
