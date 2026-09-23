from queue import Queue
from worker import RustWorker

class WorkerPool:

  def __init__(self, worker_path, size=4):
    self.workers = Queue()

    for _ in range(size):
      worker = RustWorker(worker_path)
      self.workers.put(worker)

  def calculate(self, numbers):
    worker = self.workers.get()

    try:
      return worker.calculate(numbers)

    finally:
      self.workers.put(worker)