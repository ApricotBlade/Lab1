import os
import requests


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


def geturl(p, c):
    url = f"https://yandex.ru/images/search?p={p}&text={c}&itype=jpg"
    html_page = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    return html_page

