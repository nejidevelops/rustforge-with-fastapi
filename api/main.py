import subprocess

result = subprocess.run(
  ["../worker/target/debug/worker.exe"],
  input="Hello from Python",
  text=True,
  capture_output=True,
)

print(result.stdout)