from fastapi import FastAPI
from typing import List
from database import create_start_app_handler
from models import Tasks
from schemas import TaskCreate, TaskMain


def get_application():
    app = FastAPI()
    app.add_event_handler("startup", create_start_app_handler(app))
    return app


app = get_application()


@app.post("/", response_model=TaskMain)
async def create(data: TaskCreate):
    task = await Tasks.create(**data.dict(exclude_unset=True))
    return task


@app.get("/", response_model=List[TaskMain])
async def show_all():
    tasks = await Tasks.all()
    return tasks

