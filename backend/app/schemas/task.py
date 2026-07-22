from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class TaskStatus(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    category: str = "Miscellaneous"
    priority: str = "Medium"
    estimated_duration: int | None = None
    deadline: datetime | None = None
    notes: str | None = None
    is_routine: bool = False
    routine_frequency: str | None = None


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    category: str | None = None
    priority: str | None = None
    estimated_duration: int | None = None
    deadline: datetime | None = None
    notes: str | None = None
    is_routine: bool | None = None
    routine_frequency: str | None = None


class TaskStatusUpdate(BaseModel):
    status: TaskStatus


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    category: str
    priority: str
    estimated_duration: int | None
    deadline: datetime | None
    status: TaskStatus
    completed_at: datetime | None
    notes: str | None
    created_at: datetime
    is_routine: bool
    routine_frequency: str | None

    class Config:
        from_attributes = True