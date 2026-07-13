from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
app = FastAPI()
tasks = []

class Task(BaseModel):
    title: str
    completed: bool

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: Task):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": task.completed
    }

    tasks.append(new_task)
    return new_task

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

@app.put("/tasks/{task_id}")    
def update_task(task_id: int, updated_task: Task):

    for task in tasks:

        if task["id"] == task_id:


            task["title"] = updated_task.title
            task["completed"] = updated_task.completed

            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for task in tasks:

        if task["id"] == task_id:
            tasks.remove(task)

            return {
                "message": "Task deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )