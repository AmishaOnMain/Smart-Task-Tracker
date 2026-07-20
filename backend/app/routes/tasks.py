from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.task import (
    TaskCreate,
    TaskResponse,
    TaskUpdate,
)
from app.services.task_service import TaskService
from app.auth.security import get_current_user

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