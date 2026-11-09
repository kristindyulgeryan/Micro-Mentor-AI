from pickletools import read_uint1
import uuid
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Cookie
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.models.job import ScenarioJob
from backend.schemas.job import ScenarioJobResponse

router = APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)

@router.get("/{job_id}", response_model=ScenarioJobResponse)
def get_job_status(job_id:str, db:Session=Depends(get_db)):
    job=db.query(ScenarioJob).filter(ScenarioJob.job_id == job_id).first()

    if not job:
        raise HTTPException(status_code=404,detail="Job not found")

    return job
