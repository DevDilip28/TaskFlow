from src.task.dots import TaskSchema
from sqlalchemy.orm import Session
from src.task.models import TaskModel
from fastapi import HTTPException

def create_task(body: TaskSchema, db: Session):
    data = body.model_dump()

    new_task = TaskModel(title = data["title"],
                         description = data["description"],
                         is_completed = data["is_completed"]
                         )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

def get_tasks(db: Session):
    tasks = db.query(TaskModel).all()

    return tasks

def get_task_by_id(task_id: int, db: Session):
    task = db.query(TaskModel).get(task_id)

    if(not task):
        raise HTTPException(status_code=404, detail="Task not found")

    return task
 
def update_task(task_id: int, body: TaskSchema, db: Session):
    data = body.model_dump()

    task = db.query(TaskModel).get(task_id)

    if(not task):
        raise HTTPException(status_code=404, detail="Task not found")
    
    for field, value in data.items():
        setattr(task, field, value)

    db.add(task)
    db.commit()
    db.refresh(task)

    return task

def delete_task(task_id: int, db: Session):
    task = db.query(TaskModel).get(task_id)

    if(not task):
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()

    return None
