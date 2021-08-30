import pathlib
import sys


for filename in sys.argv[1:]:
    path = pathlib.Path(filename)
    counts = (
        path.read_text().count("\n") #Number of lines
    )
