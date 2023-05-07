from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

saved_data = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/solve")
async def start_solution(data: dict):
    # Save the data to a global variable
    global saved_data
    saved_data = data

    return {"message": "POST request succeeded"}


@app.get("/get_saved_data")
async def get_saved_data():
    if not saved_data:
        raise HTTPException(status_code=404, detail="No data available")
    return saved_data
