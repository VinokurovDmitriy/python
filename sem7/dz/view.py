from tkinter import *
from tkinter import scrolledtext

from sem7.dz.controller import *

res = getResult()
window = Tk()
result = scrolledtext.ScrolledText(window, width=40, height=10)
name = Entry(window, width=10)
surName = Entry(window, width=10)
phone = Entry(window, width=10)
description = Entry(window, width=10)


def clearEnter():
    name.delete(0, END)
    surName.delete(0, END)
    phone.delete(0, END)
    description.delete(0, END)


def save():
    contactList = [name.get(), surName.get(), phone.get(), description.get()]
    saveContact(getContactDict(contactList))
    showRow()
    clearEnter()


def showColumn():
    getFormatted(getColumnFormat())


def searchName():
    getFormatted(findRows(name.get()))


def delName():
    delRows(name.get())
    getFormatted(getResult())


def delSurname():
    delRows(surName.get())
    getFormatted(getResult())


def delDescription():
    delRows(description.get())
    getFormatted(getResult())


def searchSurname():
    getFormatted(findRows(surName.get()))


def searchDescription():
    getFormatted(findRows(description.get()))


def showRow():
    getFormatted(getResult())


def getFormatted(formatted):
    result.delete(1.0, END)
    result.insert(INSERT, formatted)


def mainWindow():
    window.title("Добро пожаловать в приложение PythonRu")
    window.geometry('800x450')
    lbl1 = Label(window, text="Имя", font=("Arial Bold", 14))
    lbl1.grid(column=0, row=0, padx=25, sticky=W)
    name.grid(column=1, row=0, padx=10)
    btnSearchName = Button(window, text="Поиск", command=searchName)
    btnSearchName.grid(column=2, row=0, padx=15)
    btnDelName = Button(window, text="Удалить", command=delName)
    btnDelName.grid(column=3, row=0)
    lbl2 = Label(window, text="Фамилия", font=("Arial Bold", 14))
    lbl2.grid(column=0, row=1)
    surName.grid(column=1, row=1)
    btnSearchSurname = Button(window, text="Поиск", command=searchSurname)
    btnSearchSurname.grid(column=2, row=1)
    btnDelSurname = Button(window, text="Удалить", command=delSurname)
    btnDelSurname.grid(column=3, row=1)
    lbl3 = Label(window, text="Телефон", font=("Arial Bold", 14))
    lbl3.grid(column=0, row=2)
    phone.grid(column=1, row=2)
    lbl4 = Label(window, text="Описание", font=("Arial Bold", 14))
    lbl4.grid(column=0, row=3)
    description.grid(column=1, row=3)
    btnSearchDescription = Button(window, text="Поиск", command=searchDescription)
    btnSearchDescription.grid(column=2, row=3)
    btnDelDescription = Button(window, text="Удалить", command=delDescription)
    btnDelDescription.grid(column=3, row=3)
    result.grid(column=0, row=10, columnspan=3)
    result.insert(INSERT, getResult())
    btnSave = Button(window, text="Сохранить", command=save)
    btnSave.grid(column=0, row=4)
    btnShowColumn = Button(window, text="Вид 1", command=showColumn)
    btnShowColumn.grid(column=1, row=4)
    btnShowRow = Button(window, text="Вид 2", command=showRow)
    btnShowRow.grid(column=2, row=4)
    window.mainloop()
