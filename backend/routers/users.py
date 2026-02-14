from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schemas.user
import models.user
from dependencies.auth import get_current_user
from database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

# get current user profile
@router.get("/me", response_model=schemas.user.UserOut)
def read_users_me(current_user: models.user.User = Depends(get_current_user)):
    return current_user

# get user by id
@router.get("/{user_id}", response_model=schemas.user.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.user.User).filter(models.user.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user