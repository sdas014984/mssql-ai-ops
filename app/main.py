from fastapi import FastAPI
from app.collector import get_metrics
from app.analyzer import analyze
from app.fixer import kill_session

app = FastAPI()

@app.get("/analyze")
def run_analysis():
    metrics = get_metrics()
    result = analyze(metrics)
    return {"analysis": result}

@app.post("/fix/{session_id}")
def fix_issue(session_id: int):
    result = kill_session(session_id)
    return {"action": result}
