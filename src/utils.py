import os
from PIL import Image


def getClassList(filePath):
    file = open(filePath, "r")
    classList = file.readlines()
    classList = list(map(str.strip, classList))
    return classList


def saveImg(img, finalClass):
    # save image and class with PIL
    # check if fodlder exists otherwise create a class folder
    if not os.path.exists(f"database/{finalClass}"):
        os.makedirs(f"database/{finalClass}")

    # save image with PIL
    saveName = img.name
    img = Image.open(img)
    img.save(f"database/{finalClass}/{saveName}")
    # img.save(f"database/{finalClass}/{img.name}")
