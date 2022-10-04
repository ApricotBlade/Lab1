import os
import time
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


def saveimg(link, serialnum, imgclass):
    try:
        response = requests.get(link, timeout=1, headers={"User-Agent": "Mozilla/5.0"})
        if response:
            os.chdir(f'{imgclass}')
            name = f'{serialnum:04}.jpg'
            open(name, 'wb').write(response.content)
            os.chdir('..')
            return True
        return False
    except requests.exceptions.Timeout:
        return False
    except requests.exceptions.ConnectionError:
        return False


def bulksaving(classname, requirednum):
    print(f'Начинаю загрузку изображений класса "{classname}"')
    page = 0
    soup = BeautifulSoup(geturl(page, f'{classname}').text, "lxml")
    maxindex = 29
    index = 0
    uploadednum = 0
    while uploadednum != requirednum:
        time.sleep(0.02)
        link = str(soup.find("div", class_=f"serp-item_pos_{index}"))
        if link.find('"origin":{"') != -1:
            link = link.split('"origin":{"')
            link = link[1].split('"url":"')
            link = link[1].split('"}')
            if saveimg(link[0], uploadednum, classname):
                print(f'{round((100 * uploadednum / requirednum), 2)}%')
                uploadednum += 1
            else:
                print(f'{round((100 * uploadednum / requirednum), 2)}%')
            if index == maxindex:
                page += 1
                soup = BeautifulSoup(geturl(page, f'{classname}').text, "lxml")
                maxindex += 30
        index += 1
    print(f'Загрузка изображений класса "{classname}" в объёме {requirednum} шт. успешно завершена!')
    print("")


bulksaving('tulip', 5)
bulksaving('rose', 7)
