myList = [1, 2, 5, 3, 6, 2, 7, 8, 3]


def findMax(list):
    resultList = []
    itemMax = list[0]
    resultList = [itemMax]
    for item in myList:
        if item > itemMax:
            itemMax = item
            resultList.append(item)
    print(resultList)
findMax(myList)
