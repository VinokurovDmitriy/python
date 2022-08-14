from sem8.dz.controllers import getPlaces, getAddress, getPhones, getPupils, getNewDf
from sem8.dz.dataStorage import data

newId = 1


def init(maxId):
    global newId
    newId = maxId + 1


def delRows():
    delItems(getNewDf(getPupils()), 'csvStorage/pupils.csv')
    delItems(getNewDf(getAddress()), 'csvStorage/address.csv')
    delItems(getNewDf(getPlaces()), 'csvStorage/places.csv')
    delItems(getNewDf(getPhones()), 'csvStorage/phones.csv')


def delItems(df, fileName):
    with open(fileName, 'w', encoding='utf-8') as f:
        print
        f.write(df.to_csv(), index=0)


def addNewPupil():
    pupRow = f'{newId}, {data["name"]}, {data["surname"]}, {data["birthday"]}, {data["class"]}, {data["progress"]}\n'
    plRow = f'{newId}, {data["row"]}, {data["desk"]}, {data["variant"]}\n'
    phRow = f'{newId}, {data["phone"]}, {data["commentPhone"]}\n'
    adRow = f'{newId}, {data["address"]}, {data["commentAddress"]}\n'
    addItem('csvStorage/places.csv', plRow)
    addItem('csvStorage/address.csv', adRow)
    addItem('csvStorage/pupils.csv', pupRow)
    addItem('csvStorage/phones.csv', phRow)

def addItem(fileName, row):
    with open(fileName, 'a', encoding='utf-8') as f:
        f.write(row)

