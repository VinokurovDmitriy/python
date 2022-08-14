import pandas as pd
from sem8.dz.dataStorage import data


def getPD(fileName):
    return pd.read_csv(fileName).rename(columns=lambda x: x.strip())


def getPupils():
    return getPD('csvStorage/pupils.csv')


def showPupils():
    df_pupils = getPupils()
    return cutId(df_pupils)


def getNewDf(df):
    newDf = filterDf(df)
    return cutId(newDf)


def cutId(df):
    del df['id']
    return df


def getNameSurname():
    df_part = getPupils()[['id', 'Имя', 'Фамилия']]
    return df_part


def getPlaces():
    return getPD('csvStorage/places.csv')


def getPhones():
    return getPD('csvStorage/phones.csv')


def getAddress():
    return getPD('csvStorage/address.csv')


def filterDf(df):
    return df.loc[~df['id'].isin(data['foundedIds'])]
