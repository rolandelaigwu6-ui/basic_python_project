"""Run independent task suites; unfinished solutions are expected to fail."""
import pathlib
import subprocess
import sys
root = pathlib.Path(__file__).resolve().parent
results = []
for folder in sorted(root.iterdir()):
    if folder.is_dir() and (folder / "test_solution.py").exists():
        print("\nTask: " + folder.name, flush=True)
        result = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", ".", "-p", "test_*.py", "-v"], cwd=folder)
        results.append((folder.name, result.returncode))
print("\nVisible-suite outcomes (not exam marks):")
for name, code in results:
    print(name + ": " + ("PASS" if code == 0 else "INCOMPLETE / FAIL"))
sys.exit(0 if all(code == 0 for _, code in results) else 1)
