from pydantic import BaseModel

class BriefInput(BaseModel):
    title: str
    audience: str
    goal: str
    tone: str

class AgentResponse(BaseModel):
    strategy_summary: str
    post_text: str
    email_copy: str
    image_prompt: str
    agent_notes: str
