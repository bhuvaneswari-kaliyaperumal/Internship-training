from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
app = FastAPI()
tasks = []

# Create Task
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: Task):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": task.completed
    }

    tasks.append(new_task)
    return new_task

# Get All Tasks
@app.get("/tasks")
def get_tasks():
    return tasks


# Get One Task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# Update Task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):

    for task in tasks:

        if task["id"] == task_id:

            task["title"] = task.title
            task["completed"] = task.completed

            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# Delete Task
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