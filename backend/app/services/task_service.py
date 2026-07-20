from datetime import datetime

from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


class TaskService:

    @staticmethod
    def create_task(
        db: Session,
        user_id: int,
        task_data: TaskCreate,
    ) -> Task:

        task = Task(
            user_id=user_id,
            **task_data.model_dump(),
        )

        db.add(task)
        db.commit()
        db.refresh(task)

        return task
    
    @staticmethod
    def get_tasks(
        db: Session,
        user_id: int,
    ):

      return (
            db.query(Task)
            .filter(Task.user_id == user_id)
            .order_by(Task.created_at.desc())
            .all()
        )
    
    @staticmethod
    def get_task(
        db: Session,
        user_id: int,
        task_id: int,
    ):

        return (
            db.query(Task)
            .filter(
                Task.id == task_id,
                Task.user_id == user_id,
            )
            .first()
        )
    


    @staticmethod
    def update_task(
        db: Session,
        task: Task,
        task_data: TaskUpdate,
    ) -> Task:

        update_data = task_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(task, key, value)

        if update_data.get("completed"):
            task.completed_at = datetime.utcnow()

        elif "completed" in update_data:
            task.completed_at = None

        db.commit()
        db.refresh(task)

        return task
    


    @staticmethod
    def delete_task(
        db: Session,
        task: Task,
    ):

        db.delete(task)
        db.commit()