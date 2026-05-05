from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from f22_system.database import get_db
from f22_system.agents.context_agent import ContextAgent
from f22_system.agents.level_agent import LevelAgent
from f22_system.agents.decision_agent import DecisionAgent
from f22_system.agents.chart_agent import ChartAgent
from f22_system.agents.execution_agent import ExecutionAgent
from f22_system.agents.journal_agent import JournalAgent
from f22_system.agents.analytics_agent import AnalyticsAgent

app = FastAPI()

class WorkflowRequest(BaseModel):
    phase: str
    data: dict

@app.post("/workflow/")
async def workflow(request: WorkflowRequest, db: Session = Depends(get_db)):
    if request.phase == "morning":
        agent = ContextAgent(db)
    elif request.phase == "planning":
        agent = LevelAgent(db)
    elif request.phase == "validation":
        agent = DecisionAgent(db)
    elif request.phase == "journal":
        agent = JournalAgent(db)
    elif request.phase == "reporting":
        agent = AnalyticsAgent(db)
    else:
        raise HTTPException(status_code=400, detail="Invalid workflow phase")

    response = await agent.process(request.data)
    return response
