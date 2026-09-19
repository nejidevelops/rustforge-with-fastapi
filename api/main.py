import subprocess
import json

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from config import RUST_WORKER

app = FastAPI()

class CalculationRequest(BaseModel):
  numbers: list[int]

@app.get("/")
def root():
  return {"message":"Hello from Rust Forge"}

@app.post("/calculate")
def calculate(request: CalculationRequest):
  payload = {
    "numbers": request.numbers
  }

  json_input = json.dumps(payload)

  result = subprocess.run(
    [str(RUST_WORKER)],
    input=json_input,
    text=True,
    capture_output=True,
  )

  if result.returncode != 0:
    raise HTTPException(
      status_code=500,
      detail={
        "message": "Rust worker failed",
        "exit_code": result.returncode,
        "stderr": result.stderr,
      },
    )

  try:
    output = json.loads(result.stdout)
  except json.JSONDecodeError:
    raise HTTPException(
      status_code=500,
      detail="Rust worker returned invalid JSON",
    )

  if "error" in output:
    raise HTTPException(
      status_code=400,
      detail=output["error"],
    )

  return output