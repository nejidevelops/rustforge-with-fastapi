import subprocess
import json

from fastapi import FastAPI
from pydantic import BaseModel

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

  print(json_input)

  result = subprocess.run(
  ["../worker/target/debug/worker.exe"],
  input=json_input,
  text=True,
  capture_output=True,
  )

  output = json.loads(result.stdout)

  return output