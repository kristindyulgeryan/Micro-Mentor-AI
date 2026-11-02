import uuid
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Cookie,Response,BackgroundTasks
from sqlalchemy.engine import create
from sqlalchemy.orm import Session

from backend.db.database import get_db, SessionLocal
from backend.models.scenario import Scenario, ScenarioNode
from backend.models.job import ScenarioJob
from backend.schemas.scenario import (
    CompleteScenarioResponse, CompleteScenarioNodeResponse, CreateScenarioRequest
)
from backend.schemas.job import ScenarioJobResponse

router = APIRouter(
    prefix="/scenarios",
    tags=["scenarios"],
    )

def get_session_id(session_id: Optional[str] = Cookie(None)):
    if not session_id:
        session_id = str(uuid.uuid4())
    return session_id

@router.post("/create",response_model=ScenarioJobResponse)
def create_scenario(
    request: CreateScenarioRequest,
    background_tasks: BackgroundTasks,
    response: Response,
    session_id: str = Depends(get_session_id),
    db: Session=Depends(get_db)
):
  response.set_cookie(key="session_id", value=session_id, httponly=True)
  job_id = str(uuid.uuid4())

  job = ScenarioJob(
    job_id=job_id,
    session_id=session_id,
    theme=request.theme,
    status="pending"
  )

  db.add(job)
  db.commit()

  # TODO: add background tasks, generate scenario
  background_tasks.add_task(
    generate_scenario_task,
    job_id = job_id,
    theme = request.theme,
    session_id = session_id
  )

  return job


def generate_scenario_task(job_id: str, theme:str, session_id: str):
    db = SessionLocal()

    try:
        job = db.query(ScenarioJob).filter(ScenarioJob.job_id == job_id).first()

        if not job:
            return

        try:
            job.status = "processing"
            db.commit()

            scenario = {} # TODO: generate scenario

            job.scenario_id = 1  # TODO: update scenario
            job.status = "completed"
            job.completed_at = datetime.now()
            db.commit()
        
        except Exception as e:
            
            job.status = "failed"
            job.completed_at = datetime.now()
            job.error=str(e)
            db.commit()
    finally:
        db.close()


@router.get("/{scenario_id}/complete", response_model=CompleteScenarioResponse)
def get_complete_scenario(scenario_id: int, db:Session = Depends(get_db)):
    scenario = db.query(Scenario).filter(Scenario.id == scenario_id).first()
    if not scenario:
        raise HTTPException(status_code=404,detail="Scenario not found")
    
    # TODO pars scenario
    return scenario
