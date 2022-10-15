def getWeedList(filePath):
    file = open(filePath, "r")
    weedList = file.readlines()
    weedList = list(map(str.strip, weedList))
    return weedList
