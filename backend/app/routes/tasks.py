from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.auth.security import get_current_user
from app.database.session import get_db
from app.models.task import TaskStatus
from app.models.user import User
from app.schemas.task import (
    TaskCreate,
    TaskResponse,
    TaskStatusUpdate,
    TaskUpdate,
)
from app.services.task_service import TaskService

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

@router.post(
    "/",
    response_model=TaskResponse,
)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return TaskService.create_task(
        db=db,
        user_id=current_user.id,
        task_data=task,
    )


@router.get(
    "/",
    response_model=list[TaskResponse],
)
def get_tasks(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return TaskService.get_tasks(
        db=db,
        user_id=current_user.id,
    )

@router.get(
    "/{task_id}",
    response_model=TaskResponse,
)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    task = TaskService.get_task(
        db=db,
        user_id=current_user.id,
        task_id=task_id,
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return task



@router.put(
    "/{task_id}",
    response_model=TaskResponse,
)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    task = TaskService.get_task(
        db=db,
        user_id=current_user.id,
        task_id=task_id,
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return TaskService.update_task(
        db=db,
        task=task,
        task_data=task_data,
    )


@router.delete(
    "/{task_id}",
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    task = TaskService.get_task(
        db=db,
        user_id=current_user.id,
        task_id=task_id,
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    TaskService.delete_task(
        db=db,
        task=task,
    )

    return {
        "message": "Task deleted successfully"
    }


@router.patch("/{task_id}/status", response_model=TaskResponse)
def update_task_status(
    task_id: int,
    status_data: TaskStatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = TaskService.get_task(
        db,
        current_user.id,
        task_id,
    )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return TaskService.update_task_status(
        db,
        task,
        status_data.status,
    )


@router.get("/search", response_model=list[TaskResponse])
def search_tasks(
    query: str = Query(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return TaskService.search_tasks(
        db,
        current_user.id,
        query,
    )




@router.get("/filter", response_model=list[TaskResponse])
def filter_tasks(
    status: TaskStatus | None = None,
    priority: str | None = None,
    category: str | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return TaskService.filter_tasks(
        db,
        current_user.id,
        status,
        priority,
        category,
    )



@router.get("/today", response_model=list[TaskResponse])
def today_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return TaskService.get_today_tasks(
        db,
        current_user.id,
    )


@router.get("/upcoming", response_model=list[TaskResponse])
def upcoming_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return TaskService.get_upcoming_tasks(
        db,
        current_user.id,
    )


@router.get("/overdue", response_model=list[TaskResponse])
def overdue_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return TaskService.get_overdue_tasks(
        db,
        current_user.id,
    )