from pydantic import BaseModel


class DashboardResponse(BaseModel):
    completed_today: int
    pending_today: int
    overdue: int

    tasks_this_week: int
    tasks_this_month: int

    completion_rate: float

    current_streak: int
    longest_streak: int

    high_priority_pending: int

    productivity_score: float