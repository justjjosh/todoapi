from fastapi import APIRouter, Depends, HTTPException
from app import crud, schemas, models, auth
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.post("/register", response_model = schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@router.get("/{username}", response_model = schemas.User)
def get_user(username: str, db: Session = Depends(get_db)) -> models.User | None:
    return crud.get_user(db=db, username=username)

@router.post("/login", response_model = schemas.Token)
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    user_data = crud.get_user(db=db, username=user.username)

    if not user_data:
        raise HTTPException(status_code=401, detail="invalid credentials")
    
    valid_password = auth.verify_password(user.password, user_data.hashed_password)

    if not valid_password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = auth.create_access_token({"sub": user_data.id})

    return {"access_token": token, "token_type": "bearer"}
