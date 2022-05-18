from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field


class TaskMain(BaseModel):
    id: UUID
    task_title: str
    task_desc: str
    task_done: str
    created_at: datetime
    updated_at: datetime


class TaskCreate(BaseModel):
    task_title: str = Field(..., max_length=100)
    task_desc: str = Field(..., max_length=300)