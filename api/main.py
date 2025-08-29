from fastapi import FastAPI
from claude_agent import run_claude_agent
from schemas import BriefInput, AgentResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Claude Agent API is running"}

@app.post("/generate")
def generate_response(brief: BriefInput) -> AgentResponse:
    return run_claude_agent(brief)
