from pathlib import Path

directory = Path("./")
if "counter.txt" in directory.iterdir():
    print(True)
else:
    with open("counter.txt", "w") as f:
        data = "1"
        f.write(data)
