from queue import Queue
from worker import RustWorker

class WorkerPool:

  def __init__(self, worker_path, size=4):
    self.workers = Queue()

    for _ in range(size):
      worker = RustWorker(worker_path)
      self.workers.puts(worker)