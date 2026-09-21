import json
import subprocess
import threading

class RustWorker:

  def __init__(self, worker_path):
    self.process = subprocess.Popen(
      [str(worker_path)],
      stdin=subprocess.PIPE,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
      text=True,
      bufsize=1,
    )

    self.lock = threading.Lock()

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