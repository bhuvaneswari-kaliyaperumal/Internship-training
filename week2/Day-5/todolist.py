from fastapi import FastAPI, HTTPException, status  
from pydantic import BaseModel  

app = FastAPI()


# Request model
class TaskCreate(BaseModel):
    title: str
    completed: bool = False


# Response model
class Task(TaskCreate):
    id: int


# In-memory storage
tasks = []
next_id = 1


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    global next_id

    new_task = {
        "id": next_id,
        "title": task.title,
        "completed": task.completed
    }

    tasks.append(new_task)
    next_id += 1

    return new_task


@app.get("/tasks", response_model=list[Task])
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: TaskCreate):

    for task in tasks:

        if task["id"] == task_id:

            task["title"] = updated_task.title
            task["completed"] = updated_task.completed

            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):

    for index, task in enumerate(tasks):

        if task["id"] == task_id:

            tasks.pop(index)

            return

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
