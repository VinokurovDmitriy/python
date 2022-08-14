from tkinter import scrolledtext, INSERT


def setScrolledText(row, data, layout, height):
    scrText = scrolledtext.ScrolledText(layout, width=70, height=height)
    scrText.grid(column=0, row=row, columnspan=5)
    scrText.insert(INSERT, data)