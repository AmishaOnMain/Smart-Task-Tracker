from datetime import datetime

from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: str | None = None
    category: str = "Miscellaneous"
    priority: str = "Medium"
    estimated_duration: int | None = None
    deadline: datetime | None = None
    notes: str | None = None

    is_routine: bool = False
    routine_frequency: str | None = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    category: str | None = None
    priority: str | None = None
    estimated_duration: int | None = None
    deadline: datetime | None = None
    notes: str | None = None

    completed: bool | None = None

    is_routine: bool | None = None
    routine_frequency: str | None = None


class TaskResponse(TaskBase):
    id: int

    user_id: int

    completed: bool
    completed_at: datetime | None

    created_at: datetime

    class Config:
        from_attributes = True