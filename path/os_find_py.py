from os import getcwd, walk

extension = '.py'

count = 0
for root, directories, filenames in walk(getcwd()):
    for filename in filenames:
        if filename.endswith(extension):
            count += 1
print(f"{count} PY file found")
