FROM python:3.9-slim-buster

WORKDIR /app

RUN pip install uvicorn fastapi

COPY . .

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
