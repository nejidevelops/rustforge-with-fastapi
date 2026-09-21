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

print(worker.calculate([10, 20, 30, 40]))

print(worker.calculate([5, 10, 15]))

print(worker.calculate([100, 200, 300]))

print(worker.calculate([]))