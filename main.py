import os
import requests
from bs4 import BeautifulSoup


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
    page = f"https://yandex.ru/images/search?p={p}&text={c}&itype=jpg"
    url = requests.get(page, headers={"User-Agent": "Mozilla/5.0"})
    return url


def getlink(url, pos):
    soup = BeautifulSoup(url.text, "lxml")
    link = str(soup.find("div", class_=f"serp-item_pos_{pos}"))
    if link.find('"origin":{"') != -1:
        link = link.split('"origin":{"')
        link = link[1].split('"url":"')
        link = link[1].split('"}')
        if link[0].find('.jpg.') != -1:
            return link[0]
    return False


