from enum import Enum

from pydantic import BaseModel


class Priority(str, Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class InitialPlan(BaseModel):
    summary: str
    search_queries: list[str]
    priority: Priority
    requires_code_changes: bool