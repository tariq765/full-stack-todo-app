from fastapi import APIRouter, HTTPException, Depends, status
from sqlmodel import Session, select
from typing import List
from ..models.task import Task, TaskRead, TaskUpdate, TaskBase, TaskCreate
from ..db.session import get_session
from ..core.security import verify_token, TokenData
from ..core.config import settings

router = APIRouter()


@router.get("/tasks", response_model=List[TaskRead])
def list_tasks(
    user_id: str,
    token_data: TokenData = Depends(verify_token),
    session: Session = Depends(get_session)
):
    """List all tasks for the authenticated user."""
    # Verify that the user_id in the path matches the authenticated user
    if token_data.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User ID does not match authenticated user"
        )

    # Query tasks filtered by user_id
    statement = select(Task).where(Task.user_id == user_id)
    tasks = session.exec(statement).all()
    return tasks


@router.post("/tasks", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(
    user_id: str,
    task: TaskCreate,
    token_data: TokenData = Depends(verify_token),
    session: Session = Depends(get_session)
):
    """Create a new task for the authenticated user."""
    # Verify that the user_id in the path matches the authenticated user
    if token_data.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User ID does not match authenticated user"
        )

    # Assign user_id from authenticated user and create task
    db_task = Task(
        title=task.title,
        description=task.description,
        completed=task.completed,
        user_id=user_id
    )
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


@router.get("/tasks/{id}", response_model=TaskRead)
def get_task(
    user_id: str,
    id: int,
    token_data: TokenData = Depends(verify_token),
    session: Session = Depends(get_session)
):
    """Get a specific task by ID for the authenticated user."""
    # Verify that the user_id in the path matches the authenticated user
    if token_data.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User ID does not match authenticated user"
        )

    # Query task by id AND user_id
    statement = select(Task).where(Task.id == id).where(Task.user_id == user_id)
    db_task = session.exec(statement).first()

    # Return 404 if not found or not owned
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or does not belong to user"
        )

    return db_task


@router.put("/tasks/{id}", response_model=TaskRead)
def update_task(
    user_id: str,
    id: int,
    task_update: TaskUpdate,
    token_data: TokenData = Depends(verify_token),
    session: Session = Depends(get_session)
):
    """Update a task by ID for the authenticated user."""
    # Verify that the user_id in the path matches the authenticated user
    if token_data.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User ID does not match authenticated user"
        )

    # Query task by id AND user_id
    statement = select(Task).where(Task.id == id).where(Task.user_id == user_id)
    db_task = session.exec(statement).first()

    # Return 404 if not found or not owned
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or does not belong to user"
        )

    # Update title/description only, prevent user_id modification
    task_data = task_update.dict(exclude_unset=True)
    for field, value in task_data.items():
        setattr(db_task, field, value)

    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


@router.delete("/tasks/{id}")
def delete_task(
    user_id: str,
    id: int,
    token_data: TokenData = Depends(verify_token),
    session: Session = Depends(get_session)
):
    """Delete a task by ID for the authenticated user."""
    # Verify that the user_id in the path matches the authenticated user
    if token_data.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User ID does not match authenticated user"
        )

    # Query task by id AND user_id
    statement = select(Task).where(Task.id == id).where(Task.user_id == user_id)
    db_task = session.exec(statement).first()

    # Return 404 if not found or not owned
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or does not belong to user"
        )

    # Remove task from database
    session.delete(db_task)
    session.commit()
    return {"message": "Task deleted successfully"}


@router.patch("/tasks/{id}/complete", response_model=TaskRead)
def toggle_task_completion(
    user_id: str,
    id: int,
    token_data: TokenData = Depends(verify_token),
    session: Session = Depends(get_session)
):
    """Toggle the completion status of a task by ID for the authenticated user."""
    # Verify that the user_id in the path matches the authenticated user
    if token_data.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User ID does not match authenticated user"
        )

    # Query task by id AND user_id
    statement = select(Task).where(Task.id == id).where(Task.user_id == user_id)
    db_task = session.exec(statement).first()

    # Return 404 if not found or not owned
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or does not belong to user"
        )

    # Toggle completed boolean
    db_task.completed = not db_task.completed
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task