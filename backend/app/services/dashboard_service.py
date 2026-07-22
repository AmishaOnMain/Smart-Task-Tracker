from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.models.task import Task, TaskStatus


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