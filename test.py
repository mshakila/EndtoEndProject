# this example shows how to split path and create a folder and a file in that folder
import os

path = "folder/file.txt"

dir,file = os.path.split(path)

print(os.path.split(path))

os.makedirs(dir, exist_ok = True)

with open(path, "w") as f:
    pass

