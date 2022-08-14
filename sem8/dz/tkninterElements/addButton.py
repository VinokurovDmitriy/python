from tkinter import Button


def setButton(label, column, row, command, layout):
    btn = Button(layout, text=label, command=command)
    btn.grid(column=column, row=row, padx=15)