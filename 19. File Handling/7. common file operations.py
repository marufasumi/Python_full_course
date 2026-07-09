import os
from pathlib import Path

# os.mkdir("new_folder")
# Path("new_folder1").mkdir()

# os.remove("new.txt")
# Path("neww.txt").unlink()

# os.rename("hello.txt", "hello_new.txt")
# Path("hello_new.txt").rename("abcd.txt")

# for f in os.listdir("."):
#     print(f)

for f in Path("C:\\Users\\").iterdir():
    print(f)
