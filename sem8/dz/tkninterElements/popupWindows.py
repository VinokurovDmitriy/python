from tkinter import messagebox


def showInfo(message):
    messagebox.showinfo("Успех", message)

def showWarning(message):
    messagebox.showinfo("Внимание", message)


def showError(message):
    messagebox.showerror("Ошибка", message)
