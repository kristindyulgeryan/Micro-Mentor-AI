from sqlalchemy import Column, Integer,String,DateTime,Boolean,ForeignKey,JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from db.database import Base


class Scenario(Base):
    __tablename__ = "scenarios"

    id = Column(Integer, primary_key=True, index=True)
    title=Column(String, index=True)
    session_id= Column(String, index=True)
    created_at=Column(DateTime(timezone=True), server_default=func.now())

    nodes= relationship(argument="ScenarioNode", back_populates="scenario")


class ScenarioNode(Base):
    __tablename__ = "scenario_nodes"

    id = Column(Integer, primary_key=True, index=True)
    scenario_id=Column(Integer, ForeignKey("scenarios.id"), index=True)
    content = Column(String)
    is_root = Column(Boolean, default=False)
    is_sending = Column(Boolean, default=False)
    is_winning_ending=Column(Boolean, default=False)
    options = Column(JSON, default=list)

    scenario = relationship(argument="Scenario", back_populates="nodes")