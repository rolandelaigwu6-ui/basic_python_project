from pathlib import Path

input_path = Path("sample.txt")
text = input_path.read_text(encoding="utf-8")
print(text)