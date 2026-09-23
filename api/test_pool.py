from pathlib import Path

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

print(pool.calculate([10, 20, 30, 40]))

print(pool.calculate([5, 10, 15]))

print(pool.calculate([100, 200, 300]))

print(pool.calculate([]))