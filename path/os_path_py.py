from pathlib import Path

extension = ".py"
count = 0
for filename in Path.cwd().rglob(f"*{extension}"):
    count += 1
print(f"{count} Py files found")
