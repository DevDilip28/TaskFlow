from fastapi import APIRouter, Depends
from src.task import controller
from src.task.dots import TaskSchema
from src.utils.db import get_db

task_routes = APIRouter(prefix="/task")

@task_routes.post("/create")
def create_task(body: TaskSchema, db = Depends(get_db)):
    return controller.create_task(body, db)

@task_routes.get("/all_tasks")
def get_tasks(db = Depends(get_db)):
    return controller.get_tasks(db)

@task_routes.get("/id_{task_id}")
def get_task_by_id(task_id: int, db = Depends(get_db)):
    return controller.get_task_by_id(task_id, db)

@task_routes.put("/update/id_{task_id}")
def update_task(body: TaskSchema, task_id: int, db = Depends(get_db)):
    return controller.update_task(task_id, body, db)

@task_routes.delete("/delete/id_{task_id}")
def delete_task(task_id: int, db = Depends(get_db)):
    return controller.delete_task(task_id, db)
