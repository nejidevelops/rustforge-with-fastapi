import json
import subprocess

worker = subprocess.Popen(
  ["../worker/target/debug/worker.exe"],
  stdin=subprocess.PIPE,
  stdout=subprocess.PIPE,
  stderr=subprocess.PIPE,
  text=True,
)

jobs = [
  {"numbers": [10, 20, 30, 40]},
  {"numbers": [5, 10, 15]},
  {"numbers": [100, 200, 300]},
  {"numbers": []},
]

for job in jobs:
  message = json.dumps(job)

  worker.stdin.write(message + "\n")
  worker.stdin.flush()

  response = worker.stdout.readline()

  print("Rust", response.strip())

worker.stdin.close()
worker.wait()