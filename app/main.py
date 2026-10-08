from fastapi import FastAPI

from app import models
from app.database import engine
from app.routers import auth, expenses

# Create the database tables if they don't exist yet
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Expense Tracker API",
    description="A FastAPI CRUD app with JWT authentication. Each user manages only their own expenses.",
    version="1.0.0",
)

app.include_router(auth.router)
app.include_router(expenses.router)


@app.get("/", tags=["Root"])
def root():
    return {"message": "Expense Tracker API is running. Open /docs to try it."}