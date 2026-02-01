from app.auth import get_current_user
from app import crud, schemas
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter
from app.database import get_db

router = APIRouter()

@router.get("/")
def get_todos(
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    return crud.get_todos(db=db)
    
@router.get("/{todo_id}")
def get_todo(
    todo_id: int, 
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    return crud.get_todo(db=db, todo_id=todo_id)

@router.post("/")
def create_todo(
    todo: schemas.TodoCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    return crud.create_todo(db=db, todo=todo, user_id=current_user)
    
@router.put("/{todo_id}")
def update_todo(
    todo: schemas.TodoUpdate,
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    return crud.update_todo(db=db, todo_id=todo_id, todo=todo)

@router.delete("/{todo_id}")
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    return crud.delete_todo(db=db, todo_id=todo_id)