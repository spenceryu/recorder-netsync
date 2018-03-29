def readFile(path):
    with open(path, "r") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "a") as f:
        f.write(contents)
