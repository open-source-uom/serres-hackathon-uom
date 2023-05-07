from fastapi import FastAPI
from fastapi import HTTPException
from dotenv import load_dotenv, dotenv_values
import requests

load_dotenv()
localhost = dotenv_values(".env")["LOCALHOST"]

app = FastAPI()


@app.post("/start_solution")
async def start_solution():
    # Make the POST request
    response = requests.post(f'http://{localhost}/start_solution', json={"data": "my-data"})

    # Check the response status code
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Request failed")

    # Set the value of the global variable to the response data
    solution_response = response.json()

    return {"message": "POST request succeeded"}
