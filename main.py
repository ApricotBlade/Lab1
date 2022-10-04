import os


if not os.path.isdir("dataset"):
    os.mkdir("dataset")
    os.chdir("dataset")
    os.mkdir("rose")
    os.mkdir("tulip")
else:
    os.chdir("dataset")
    if not os.path.isdir("rose"):
        os.mkdir("rose")
    if not os.path.isdir("tulip"):
        os.mkdir("tulip")