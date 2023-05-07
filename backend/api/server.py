from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
import sys
# from .. import api
import sys
import time

from typing import Callable, Any, Tuple

sys.path.append("/backend/core")
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
    # UNCOMMENT AUTO EDW
    # TA HOLES THELOUN ME MOD KAI DIV NA GINOUN X,Y
    start_time = time.time()
    string_arr,runtime = run(letters, lines, columns, holes, is_rotated)
    end_time = time.time()
    # COMMENT AUTA EDW
    # string_solution = "FFLLI YFFLI YFTLI YFTLI YTTTI"
    # string_arr = [string_solution]
    # EDW PAEI STO SOLUTIONS TA POLLA STO SOLUTION TO MONO(TO SOLUTION DEN EINAI ANAGKAIO ISA ISA TO EKANA COMMENT OUT APO
    # TO FRONTEND)
    # STO FRONTEND EXW KANEI DUPLICATE GIA NA MPOROYME NA VLEPOUME POLLAPLA THA XREIASTEI NA AFAIRETHEI KATI
    return {"message": "POST request succeeded","solutions": string_arr,"time":15.0,"solution":string_solution}


@app.get("/get_saved_data")
async def get_saved_data():
    if not saved_data:
        raise HTTPException(status_code=404, detail="No data available")
    return saved_data
