from fastapi import FastAPI
from .routes import router
from .database import engine
from . import models

# Create all tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recipe API"}
