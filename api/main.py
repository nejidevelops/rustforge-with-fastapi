from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from config import RUST_WORKER
from worker import WorkerPool

app = FastAPI()

class CalculationRequest(BaseModel):
  numbers: list[int]

rust_worker = WorkerPool(RUST_WORKER, size=4)

@app.get("/")
def root():
  return {"message":"Hello from Rust Forge"}

@app.post("/calculate")
def calculate(request: CalculationRequest):
  output = rust_worker.calculate(request.numbers)

  if "error" in output:
    raise HTTPException(
      status_code=400,
      detail=output["error"]
    )

  return output