from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.models.task import Task, TaskStatus

from collections import defaultdict
from datetime import datetime, timedelta


class DashboardService:

    @staticmethod
    def get_dashboard(
        db: Session,
        user_id: int,
    ):
        today = datetime.utcnow().date()

        tasks = (
          db.query(Task)
          .filter(Task.user_id == user_id)
          .all()
        )



        completed_today = sum(
        1
        for task in tasks
        if task.completed_at
        and task.completed_at.date() == today
        )

        pending_today = sum(
        1
        for task in tasks
        if (
        task.deadline
        and task.deadline.date() == today
        and task.status != TaskStatus.COMPLETED
        )
        )

        overdue = sum(
        1
        for task in tasks
        if (
        task.deadline
        and task.deadline.date() < today
        and task.status != TaskStatus.COMPLETED
      )
      ) 
            
        week_start = today - timedelta(days=today.weekday())

        tasks_this_week = sum(
        1
        for task in tasks
        if task.created_at.date() >= week_start
        )



        tasks_this_month = sum(
        1
        for task in tasks
        if (
        task.created_at.year == today.year
        and task.created_at.month == today.month
        )
      )
        

        total_tasks = len(tasks)

        completed_tasks = sum(
        1
        for task in tasks
        if task.status == TaskStatus.COMPLETED
        )

        completion_rate = (
        (completed_tasks / total_tasks) * 100
        if total_tasks > 0
        else 0
      )
        

        high_priority_pending = sum(
        1
        for task in tasks
        if (
        task.priority == "High"
        and task.status != TaskStatus.COMPLETED
        )
      )
        current_streak = 0
        longest_streak = 0

        productivity_score = round(
          (
          completion_rate
        - (overdue * 5)
          ),
          2,
          )

        productivity_score = max(0, min(100, productivity_score))


        return {
    "completed_today": completed_today,
    "pending_today": pending_today,
    "overdue": overdue,
    "tasks_this_week": tasks_this_week,
    "tasks_this_month": tasks_this_month,
    "completion_rate": completion_rate,
    "current_streak": current_streak,
    "longest_streak": longest_streak,
    "high_priority_pending": high_priority_pending,
    "productivity_score": productivity_score,
}
    


@staticmethod
def get_weekly_chart(
    db: Session,
    user_id: int,
):
    today = datetime.utcnow().date()
    start = today - timedelta(days=6)

    tasks = (
        db.query(Task)
        .filter(
            Task.user_id == user_id,
            Task.completed_at.is_not(None),
        )
        .all()
    )

    chart = defaultdict(int)

    for task in tasks:
        completed_date = task.completed_at.date()

        if completed_date >= start:
            chart[str(completed_date)] += 1

    result = []

    for i in range(7):
        day = start + timedelta(days=i)

        result.append(
            {
                "date": str(day),
                "completed": chart[str(day)],
            }
        )

    return result