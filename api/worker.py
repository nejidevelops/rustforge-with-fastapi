import json
import subprocess
import threading
from pathlib import Path
from queue import Empty, Queue

class WorkerError(RuntimeError):
  """Raised when a Rust worker fails or stops responding."""

class RustWorker:
  def __init__(self, worker_path, timeout=5.0):
    self.worker_path = str(worker_path)
    self.timeout = timeout
    self.lock = threading.Lock()
    self.process = None
    self.responses = None

    self._start_process()

  def _start_process(self):
    """Start Rust and create a queue for its responses."""
    self.process = subprocess.Popen(
      [self.worker_path],
      stdin=subprocess.PIPE
      stdout=subprocess.PIPE
      stderr=subprocess.DEVNULL,
      text=True,
      bufsize=1,
    )

    self.responses = Queue()

    threading.Thread(
      target=self._read_responses,
      args=(self.process, self.responses),
      daemon=True,
    ).start()

    @staticmethod































  def calculate(self, numbers):
    with self.lock:
      payload = {
        "numbers": numbers
      }

      message = json.dumps(payload)

      self.process.stdin.write(message + "\n")
      self.process.stdin.flush()

      response = self.process.stdout.readline()

      return json.loads(response)