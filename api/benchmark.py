import time
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

times = []

for _ in range(10):

  start = time.perf_counter()

  result = worker.calculate(numbers)

  end = time.perf_counter()

  times.append(end - start)

# elapsed = end - start

average = sum(times) / len(times)

print(result)

print(f"Average: {average:.4f} seconds")