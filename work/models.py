from tortoise import fields
from tortoise.models import Model
# from tortoise.contrib.pydantic import pydantic_model_creator


class Tasks(Model):
    id = fields.UUIDField(pk=True)
    task_title = fields.CharField(max_length=100)
    task_desc = fields.CharField(max_length=300)
    task_done = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


# Tasks_Pydantic = pydantic_model_creator(Tasks, name="Tasks")
# TasksIn_Pydantic = pydantic_model_creator(Tasks, name="TasksIn", exclude_readonly=True)