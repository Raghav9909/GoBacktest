from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import yfinance as yf
from alpaca_wrapper import get_data, convert_data_to_list
from google_sheet_upload import upload_sheet
import httpx
import os
# from json import jsonify
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from http://localhost:3000 (or '*' for any domain)
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],      # or specify ["GET", "POST"] etc.
    allow_headers=["*"],      # or specify ["Content-Type", "Authorization"] etc.
)

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
from pydantic import BaseModel
class tf(BaseModel):
    num:int
    unit:str
class data(BaseModel):
    ticker: str
    start_date: str
    end_date: str
    strategy:str
    timeframe: tf
@app.post("/posting_stock_info")
async def create_dataset(payload :data):
    # print(payload)
    ticker =payload.ticker
    start_date=payload.start_date
    end_date=payload.end_date
    time_frame=payload.timeframe
    strategy=payload.strategy
    bars=get_data(ticker,start_date,end_date,time_frame)
    # print(bars)
    try:
        convert_data_to_list(bars, ticker=ticker)
        upload_sheet(f"{ticker}_backtest.csv", "backtest")
    except Exception as e:
        print(f"An error occurred: {e}")
    return bars

    # async with httpx.AsyncClient() as client:
    #     response = await client.post(GOLANG_URL, json=bars)

    # # Return response from the external API
    # return {
    #     "status_code": response.status_code,
    #     "response": response.json()
    # }

