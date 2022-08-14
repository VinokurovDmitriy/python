from tkinter import ttk

from sem8.dz.controllers.viewController import elementBuilder


def addTab(label, tabData, tab_control):
    tab = ttk.Frame(tab_control, name=label)
    tab_control.add(tab, text=label)
    for item in tabData:
        elementBuilder(item, tab)
