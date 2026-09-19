from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RUST_WORKER = BASE_DIR / "worker" / "target" / "debug" / "worker.exe"