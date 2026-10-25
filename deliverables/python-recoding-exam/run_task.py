"""Run one task in its own Python process."""
import pathlib
import subprocess
import sys
root = pathlib.Path(__file__).resolve().parent
allowed = {p.name for p in root.iterdir() if p.is_dir() and (p / "test_solution.py").exists()}
if len(sys.argv) != 2 or sys.argv[1] not in allowed:
    print("Usage: python run_task.py TASK_FOLDER\nAvailable: " + ", ".join(sorted(allowed)))
    sys.exit(2)
result = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", ".", "-p", "test_*.py", "-v"], cwd=root / sys.argv[1])
sys.exit(result.returncode)
