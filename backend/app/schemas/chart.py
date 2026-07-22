from pydantic import BaseModel



class WeeklyChartItem(BaseModel):
    date: str
    completed: int


class CategoryChartItem(BaseModel):
    category: str
    count: int


class PriorityChartItem(BaseModel):
    priority: str
    count: int




