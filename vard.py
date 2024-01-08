from interpreter import run
from sys import argv
import os

if len(argv) != 2:
    print("Usage: py vard.py <filepath>")
    exit()

filepath = argv[1]
file_name, file_extension = os.path.splitext(filepath)

if file_extension != ".vard":
    print("Not a .vard file!")
    exit()

with open(filepath, "r") as f:
    script = f.read()
    run(filepath,script)