from sem7.dz.model import *


def saveContact(newContact):
    if newContact['name'] and newContact['phone']:
        with open('PB.txt', 'a', encoding='utf-8') as f:
            init(newContact)
            f.write(rowFormat())


def getResult():
    with open('PB.txt', 'r', encoding='utf-8') as f:
        return f.read()


def findRows(value):
    with open('PB.txt', 'r', encoding='utf-8') as f:
        resList = f.read().splitlines()
        resultSearch = list(filter(lambda item: item.split(';')[0] == value, resList))
        return '\n'.join(resultSearch)


def delRows(value):
    with open('PB.txt', 'r', encoding='utf-8') as f:
        resList = f.read().splitlines()
        resultSearch = list(filter(lambda item: item.split(';')[0] != value, resList))
    with open('PB.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(resultSearch))


def getColumnFormat():
    with open('PB.txt', 'r', encoding='utf-8') as f:
        resList = f.read().splitlines()
        res = ''
        for item in resList:
            init(getContactDict(item.split(';')))
            res += columnFormat()
        return res
