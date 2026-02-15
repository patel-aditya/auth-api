from fastapi import FastAPI
from models import user
from database import engine
from routers import users, auth
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Authentication - API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user.Base.metadata.create_all(bind = engine)

app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Backend is running...."}