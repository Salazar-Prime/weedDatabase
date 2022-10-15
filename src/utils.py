def getWeedList(filePath):
    file = open(filePath, "r")
    weedList = file.readlines()
    return weedList
