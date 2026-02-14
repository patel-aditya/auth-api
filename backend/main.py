from fastapi import FastAPI
from models import user
from database import engine
from routers import users, auth


app = FastAPI(title="Authentication - API")

user.Base.metadata.create_all(bind = engine)

app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Backend is running...."}