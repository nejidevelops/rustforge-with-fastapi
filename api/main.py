import subprocess

result = subprocess.run(
  ["../worker/target/debug/worker.exe"],
  input='{"numbers":[10,20,30,40]}',
  text=True,
  capture_output=True,
)

print("Rust stdout:")
print(result.stdout)

print("Rust stderr:")
print(result.stderr)

print("Rust exit code:")
print(result.returncode)  