import os
import sys
from pathlib import Path

fileName = Path("counter.txt")
if fileName.is_file():
    with open("counter.txt", "r+") as f:
        content = f.read()
        if content.isnumeric():
            f.seek(0)
            f.write(str(int(content) + 1))
        else:
            sys.exit(1)
else:
    with open("counter.txt", "w") as f:
        data = "1"
        f.write(data)
        os.chmod("counter.txt", 0o777)
        sys.exit(0)

