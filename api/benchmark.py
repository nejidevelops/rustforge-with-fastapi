import time
import json
import subprocess
from pathlib import Path

from worker import RustWorker

RUST_WORKER = (
  Path(__file__).resolve().parent
  / ".."
  / "worker"
  / "target"
  / "debug"
  / "worker.exe"
)

worker = RustWorker(RUST_WORKER)

numbers = list(range(100))

def subprocess_calculation(numbers):
  payload = {
    "numbers": numbers
  }

  json_input = json.dumps(payload)

  result = subprocess.run(
    [str(RUST_WORKER)],
    input=json_input,
    text=True,
    capture_output=True,
  )

  return json.loads(result.stdout)

times = []

for _ in range(10):

  start = time.perf_counter()

  # result = worker.calculate(numbers)

  subprocess_calculation(numbers)

  end = time.perf_counter()

  times.append(end - start)

# elapsed = end - start

average = sum(times) / len(times)

# print(result)

print(f"Average: {average:.4f} seconds")