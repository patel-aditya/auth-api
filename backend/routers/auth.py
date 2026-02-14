from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from database import get_db
import models.user
import schemas.user
import schemas.token

from cores.security import (hash_password, verify_password, create_access_token)

router = APIRouter(prefix="/auth", tags = ["Auth"])

# register
@router.post("/register", response_model= schemas.user.UserOut, status_code=status.HTTP_201_CREATED)
def register(user: schemas.user.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.user.User).filter(models.user.User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    new_user = models.user.User(username = user.username, email = user.email, hashed_password = hash_password(user.password))
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# login
@router.post("/login", response_model=schemas.token.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(models.user.User).filter(models.user.User.email == form_data.username).first()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    
    if not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    access_token = create_access_token({"user_id":db_user.id})

    return {
        "access_token":access_token,
        "token_type":"bearer",
    }
