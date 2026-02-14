from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str = Field(max_length = 72)


class UserLogin(BaseModel): 
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    # created_at: datetime
    
    class Config:
        from_attributes = True