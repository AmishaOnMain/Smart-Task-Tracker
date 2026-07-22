from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.models.task import Task, TaskStatus
from app.schemas.task import TaskCreate, TaskUpdate

from sqlalchemy import or_


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

        if "status" in update_data:
            if task.status == TaskStatus.COMPLETED:
                task.completed_at = datetime.utcnow()
            else:
                task.completed_at = None

        db.commit()
        db.refresh(task)

        return task
    
    @staticmethod
    def update_task_status(
    db: Session,
    task: Task,
    status: TaskStatus,
    ) -> Task:

        task.status = status

        if status == TaskStatus.COMPLETED:
            task.completed_at = datetime.utcnow()
        else:
            task.completed_at = None

        db.commit()
        db.refresh(task)

        return task
    
    @staticmethod
    def search_tasks(
    db: Session,
    user_id: int,
    query: str,
    ):

        return (
            db.query(Task)
            .filter(
                Task.user_id == user_id,
                or_(
                    Task.title.ilike(f"%{query}%"),
                    Task.description.ilike(f"%{query}%"),
            ),
        )
        .all()
    )


    @staticmethod
    def filter_tasks(
    db: Session,
    user_id: int,
    status: TaskStatus | None = None,
    priority: str | None = None,
    category: str | None = None,
    ):

        query = db.query(Task).filter(Task.user_id == user_id)

        if status:
            query = query.filter(Task.status == status)

        if priority:
            query = query.filter(Task.priority == priority)

        if category:
            query = query.filter(Task.category == category)

        return query.all()

    @staticmethod
    def delete_task(
        db: Session,
        task: Task,
    ):

        db.delete(task)
        db.commit()



    @staticmethod
    def get_today_tasks(
    db: Session,
    user_id: int,
    ):
        today = datetime.utcnow().date()

        tasks = (
            db.query(Task)
            .filter(
                Task.user_id == user_id,
                Task.deadline.is_not(None),
        )
        .all()
    )

        return [
        task
        for task in tasks
        if task.deadline.date() == today
        ]
    


    @staticmethod
    def get_upcoming_tasks(
    db: Session,
    user_id: int,
):
        today = datetime.utcnow().date()

        tasks = (
        db.query(Task)
        .filter(
            Task.user_id == user_id,
            Task.deadline.is_not(None),
        )
        .all()
    )

        return [
        task
        for task in tasks
        if task.deadline.date() > today
        ]
    



    @staticmethod
    def get_overdue_tasks(
    db: Session,
    user_id: int,
):
        today = datetime.utcnow().date()

        tasks = (
        db.query(Task)
        .filter(
            Task.user_id == user_id,
            Task.deadline.is_not(None),
        )
        .all()
    )

        return [
        task
        for task in tasks
        if (
            task.deadline.date() < today
            and task.status != TaskStatus.COMPLETED
        )
        ]


    