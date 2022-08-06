from tkinter import *


def setLabel(label, column, row, layout):
    lbl = Label(layout, text=label, font=("Arial Bold", 14))
    lbl.grid(column=column, row=row, padx=(10, 10), pady=(10, 0), sticky=W)
