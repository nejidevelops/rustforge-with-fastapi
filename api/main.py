import subprocess
import json

payload = {
  "numbers": [10,20,30,40]
}

json_input = json.dumps(payload)

print(json_input)
result = subprocess.run(
  ["../worker/target/debug/worker.exe"],
  input=json_input,
  text=True,
  capture_output=True,
)

print("Rust stdout:")
print(result.stdout)

print("Rust stderr:")
print(result.stderr)

print("Rust exit code:")
print(result.returncode)

if result.returncode == 0:
  output = json.loads(result.stdout)

  print("Parsed Result:")
  print(output)