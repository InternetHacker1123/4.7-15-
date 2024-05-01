from tkinter import *

root = Tk()
num1 = Entry()
num2 = Entry()


def add(event):
    try:
        num1_value = int(num1.get())
        num2_value = int(num2.get())
        lab["text"] = str(num1_value + num2_value)
    except:
        lab["text"] = "Ошибка"


def sub(event):
    try:
        num1_value = int(num1.get())
        num2_value = int(num2.get())
        lab["text"] = str(num1_value - num2_value)
    except:
        lab["text"] = "Ошибка"


def mult(event):
    try:
        num1_value = int(num1.get())
        num2_value = int(num2.get())
        lab["text"] = str(num1_value * num2_value)
    except:
        lab["text"] = "Ошибка"


def div(event):
    try:
        num1_value = int(num1.get())
        num2_value = int(num2.get())
        lab["text"] = str(num1_value / num2_value)
    except:
        lab["text"] = "Ошибка"


but1 = Button(text="+", width=20, pady=2)
but2 = Button(text="-", width=20, pady=2)
but3 = Button(text="*", width=20, pady=2)
but4 = Button(text="/", width=20, pady=2)
lab = Label()


but1.bind("<Button-1>", add)
but2.bind("<Button-1>", sub)
but3.bind("<Button-1>", mult)
but4.bind("<Button-1>", div)

num1.pack()
num2.pack()
but1.pack()
but2.pack()
but3.pack()
but4.pack()
lab.pack()

root.mainloop()
