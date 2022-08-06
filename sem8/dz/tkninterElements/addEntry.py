from tkinter import Entry


def setEntry(name, column, row, layout):
    entry = Entry(layout, width=20, name=name)
    entry.grid(column=column, padx=(10, 10), pady=(0, 10), row=row)
