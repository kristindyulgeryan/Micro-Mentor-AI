from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class ScenarioOptionLLM(BaseModel):
    text: str=Field(description="the text of the option shown to the user")
    nextNode: Dict[str,Any] = Field(description="the next node content and its options")


class ScenarioNodeLLM(BaseModel):
    content: str=Field(description="The main content of the scenario node")
    isEnding: bool = Field(description="Whether this node is an ending node")
    isWinningEnding: bool = Field(description="Whether this node is a winning ending node")
    options: Optional[List[ScenarioOptionLLM]] = Field(default=None,description="The options for this node")

class ScenarioLLMResponse(BaseModel):
    title: str = Field(description="The title of the scenario")
    rootNode: ScenarioNodeLLM = Field(description="The root node of the scenario")