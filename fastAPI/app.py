from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import yfinance as yf
from alpaca_wrapper import get_data
import httpx

app = FastAPI()

GOLANG_URL='http://localhost:8080/backtest'

# Task Model
class Task(BaseModel):
    id: int
    title: str
    description: str = None
    completed: bool = False

# In-memory database
tasks: List[Task] = []

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}

# Get all tasks
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

# Get a single task by ID
# @app.get("/tasks/{task_id}", response_model=Task)
# def get_task(task_id: int):
#     task = next((task for task in tasks if task.id == task_id), None)
#     if not task:
#         raise HTTPException(status_code=404, detail="Task not found")
#     return task

# Create a new task
@app.post("/posting_stock_info")
async def create_dataset(payload):
    ticker =payload["ticker"]
    start_date=payload["start_date"]
    end_date=payload["end_date"]
    time_frame=payload["time_frame"]
    bars=get_data(ticker,start_date,end_date,time_frame)
    print(bars)
    async with httpx.AsyncClient() as client:
        response = await client.post(GOLANG_URL, json=bars)

    # Return response from the external API
    return {
        "status_code": response.status_code,
        "response": response.json()
    }

