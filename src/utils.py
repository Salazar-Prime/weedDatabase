def getClassList(filePath):
    file = open(filePath, "r")
    classList = file.readlines()
    classList = list(map(str.strip, classList))
    return classList
