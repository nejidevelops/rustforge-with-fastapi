import time
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

pool = WorkerPool(
  RUST_WORKER,
  size=4
)

numbers = list(range(100))

def run_job():
  return pool.calculate(numbers)

start = time.perf_counter()

with ThreadPoolExecutor(max_workers=4) as executor:

  futures = [
    executor.submit(run_job)
    for _ in range(4)
  ]

  results = [
    future.result()
    for future in futures
  ]

end = time.perf_counter()

print(results)

print(
  f"Total time: {end - start:.4f}s"
)

