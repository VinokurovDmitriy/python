from tkinter import END, INSERT

from sem8.dz.controllers import getNameSurname, getPupils, getPlaces, showPupils, getAddress, getPhones, cutId
from sem8.dz.dataStorage import data, dataTranslate
from sem8.dz.modelCsv import addNewPupil as addP, init as init_m, delRows
from sem8.dz.tkninterElements import setLabel, setScrolledText, setEntry, setButton
from sem8.dz.tkninterElements.popupWindows import showInfo, showError, showWarning
from sem8.dz.modelDataStorage import init as ds_init, setData

wnd = object
toolsTabName = dataTranslate['addOrDelete']


def init(w):
    global wnd
    wnd = w


def findPupil(param):
    searchValue = wnd.children['!notebook'].children[dataTranslate['addOrDelete']].children[param].get().strip().lower()
    result = getPupils().loc[getPupils()[dataTranslate[param]].str.strip().str.lower() == searchValue]
    if len(result):
        ds_init('foundedIds', result['id'].tolist())
        setData()
        reloadTabToolsScrolledText(cutId(result))
        # scrolledText = wnd.children['!notebook'].children[toolsTabName].children['!frame'].children['!scrolledtext']
        # reloadTab(scrolledText, cutId(result))
    else:
        showWarning("Такого ученика нет в базе")

def reloadTabToolsScrolledText(newText):
    scrolledText = wnd.children['!notebook'].children[toolsTabName].children['!frame'].children['!scrolledtext']
    reloadTab(scrolledText, newText)
def delPupil():
    delRows()
    allScrollTextReload()
    reloadTabToolsScrolledText('')
    showInfo(f'Ученик успешно удален')



def showDfMerged(dfOrigin):
    name_surname = getNameSurname()
    df_merged = name_surname.merge(dfOrigin)
    del df_merged['id']
    return df_merged


def getAll():
    return getPupils().merge(getPlaces())


def checkInput():
    result = ''
    for key, value in data.items():
        if value == '':
            result += dataTranslate[key] + '; '
    return result


def setAllParams():
    toolsTabWidgets = wnd.children['!notebook'].children[toolsTabName].children
    for item in toolsTabWidgets:
        if item in data:
            ds_init(item, toolsTabWidgets[item].get())
            setData()
    passInput = checkInput()
    if not passInput:
        init_m(getPupils()["id"].max())
        addP()
        allEntryClear()
        allScrollTextReload()
        showInfo(f'Ученик {data["name"]} {data["surname"]} успешно добавлен')
    else:
        showError("Вы не ввели " + passInput)


def allEntryClear():
    widgets = wnd.children['!notebook'].children[toolsTabName].children
    for item in widgets:
        if item in data:
            widgets[item].delete(0, END)


def allScrollTextReload():
    tabs = wnd.children['!notebook'].children
    for tabName in tabs:
        if tabName != dataTranslate['addOrDelete']:
            tab = tabs[tabName].children['!frame'].children['!scrolledtext']
            res = {
                tabName == dataTranslate['pupils']: reloadTab(tab, showPupils()),
                tabName == dataTranslate['place']: reloadTab(tab, showDfMerged(getPlaces())),
                tabName == dataTranslate['addressBook']: reloadTab(tab, showDfMerged(getAddress())),
                tabName == dataTranslate['contactPhones']: reloadTab(tab, showDfMerged(getPhones()))
            }[True]


def reloadTab(tab, content):
    tab.delete(1.0, END)
    tab.insert(INSERT, content)


def elementBuilder(item, currentTab):
    match (item['type']):
        case 'label':
            setLabel(item['label'], item['column'], item['row'], currentTab)
        case 'scrolledtext':
            height = item['height'] if 'height' in item else 20

            setScrolledText(item['row'], item['data'], currentTab, height=height)
        case 'entry':
            setEntry(item['name'], item['column'], item['row'], currentTab)
        case 'button':
            setButton(item['label'], item['column'], item['row'], item['command'], currentTab)
