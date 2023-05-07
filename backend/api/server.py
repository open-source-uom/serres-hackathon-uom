from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
import time

import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

from backend_core.dfs import run


from typing import Callable, Any, Tuple


sys.path.append("/backend/backend_core/dfs")
# import canvas
app = FastAPI()

def measure_time(func: Callable[..., Any], *args: Tuple[Any], **kwargs: Any) -> Any:
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    running_time = end_time - start_time
    #print(f"Function {func.__name__} took {running_time:.6f} seconds to run.")
    return result, running_time

saved_data = None
# define CORS policy
# https://fastapi.tiangolo.com/tutorial/cors/

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:8082",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # allow all methods
    allow_headers=["*"],  # allow all headers
)

@app.post("/")
async def root():
    return {"message": "Hello World"}


def measure_time(func: Callable[..., Any], *args: Tuple[Any], **kwargs: Any) -> Tuple[ any, float]:
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    running_time = end_time - start_time
    return result, running_time


@app.post("/solve")
async def start_solution(request: Request):
    # Save the data to a global variable
    # global saved_data
    # saved_data = data
    body = await request.json()
    print(body)
    lines = body["rows"]
    holes = body["holes"]
    columns = body["columns"]
    letters = body["letterList"]
    is_rotated = body["isRotated"]
    print(lines, holes, columns, is_rotated,letters)
    start_time  = time.time()
    string_arr = run(letters, lines, columns, holes, is_rotated)
    end_time = time.time()
    print("RUNTIME",end_time-start_time)
    runtime = end_time-start_time
    return {"message": "POST request succeeded","solutions": string_arr,"time":runtime,"solution":string_arr}


@app.get("/get_saved_data")
async def get_saved_data():
    if not saved_data:
        raise HTTPException(status_code=404, detail="No data available")
    return saved_data
