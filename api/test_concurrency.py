from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

from worker_pool import WorkerPool

RUST_WORKER = (
  Path(__file__).resolve().parent
  / ".."
  / "worker"
  / "target"
  / "debug"
  / "worker.exe"
)

pool = WorkerPool(RUST_WORKER, size=4)

jobs = [
    [10, 20, 30, 40],
    [5, 10, 15],
    [100, 200, 300],
    [1, 2, 3, 4],
]

def run_job(numbers):
  return pool.calculate(numbers)

with ThreadPoolExecutor(max_workers=4) as executor:
  results =  executor.map(run_job, jobs)

for result in results:
  print(result)
