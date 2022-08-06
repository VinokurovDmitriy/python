from tkinter import *
from tkinter import ttk
from sem8.dz.controllers import init
from sem8.dz.dataStorage import dataTranslate
from sem8.dz.tabsData import pupilsData, placeData, contactPhonesData, addressBookData, addPupilData
from sem8.dz.tkninterElements.addTab import addTab

window = Tk()
tab_control = ttk.Notebook(window)
init(window)


def mainWindow():
    window.title("Ведомость учеников")
    window.geometry('800x600')
    addTab(dataTranslate['pupils'], pupilsData, tab_control)
    addTab(dataTranslate['place'], placeData, tab_control)
    addTab(dataTranslate['contactPhones'], contactPhonesData, tab_control)
    addTab(dataTranslate['addressBook'], addressBookData, tab_control)
    addTab(dataTranslate['addOrDelete'], addPupilData, tab_control)
    tab_control.pack(expand=1, fill='both')
    window.mainloop()
