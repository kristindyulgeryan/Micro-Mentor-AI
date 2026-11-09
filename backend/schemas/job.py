from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class ScenarioJobBase(BaseModel):
    theme: str


class ScenarioJobResponse(BaseModel):
    job_id: str
    status: str
    created_at: datetime
    story_id: Optional[int] = None
    completed_at: Optional[datetime] = None
    error: Optional[str] = None

    class Config:
        from_attributes = True

class ScenarioJobCreate(ScenarioJobBase):
    pass


