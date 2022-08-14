from sem8.dz.dataStorage import data

key = ''
value = ''


def init(k, v):
    global key
    global value

    key = k
    value = v


def setData():
    data[key] = value

