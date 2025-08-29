import requests
from schemas import BriefInput, AgentResponse

ANTHROPIC_API_KEY = "YOUR_ANTHROPIC_API_KEY"
CLAUDE_API_URL = "https://api.anthropic.com/v1/messages"

def run_claude_agent(brief: BriefInput) -> AgentResponse:
    prompt = f"""
You are a campaign strategist.

Generate:
- A one-paragraph strategy summary
- A short social post
- An email copy (3-5 sentences)
- A DALL·E image prompt
Return in this JSON format:
{{
  "strategy_summary": "...",
  "post_text": "...",
  "email_copy": "...",
  "image_prompt": "...",
  "agent_notes": "..."
}}

Brief info:
Title: {brief.title}
Audience: {brief.audience}
Goal: {brief.goal}
Tone: {brief.tone}
"""

    headers = {
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }

    data = {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(CLAUDE_API_URL, json=data, headers=headers)
    content = response.json()["content"][0]["text"]

    # Convert raw JSON text back into dict
    parsed = eval(content)  # For simplicity; use `json.loads` with sanitised input in prod

    return AgentResponse(**parsed)
