from tkinter import *

root = Tk()
color_abc = Entry()


def showColor(event):
    but1_color = "красный"
    but2_color = "оранжевый"
    but3_color = "желтый"
    but4_color = "зеленый"
    but5_color = "голубой"
    but6_color = "синий"
    but7_color = "фиолетовый"
    try:
        color_abc.delete(0, END)
        bg_color = event.widget.cget("bg")
        match bg_color:
            case "#ff0000":
                lab["text"] = but1_color
                color_abc.insert(0, bg_color)
            case "#ff7d00":
                lab["text"] = but2_color
                color_abc.insert(0, bg_color)
            case "#ffff00":
                lab["text"] = but3_color
                color_abc.insert(0, bg_color)
            case "#00ff00":
                lab["text"] = but4_color
                color_abc.insert(0, bg_color)
            case "#007dff":
                lab["text"] = but5_color
                color_abc.insert(0, bg_color)
            case "#0000ff":
                lab["text"] = but6_color
                color_abc.insert(0, bg_color)
            case "#7d00ff":
                lab["text"] = but7_color
                color_abc.insert(0, bg_color)

    except:
        lab["text"] = "Ошибка"


but1 = Button(text="", width=20, pady=5, bg="#ff0000")
but2 = Button(text="", width=20, pady=5, bg="#ff7d00")
but3 = Button(text="", width=20, pady=5, bg="#ffff00")
but4 = Button(text="", width=20, pady=5, bg="#00ff00")
but5 = Button(text="", width=20, pady=5, bg="#007dff")
but6 = Button(text="", width=20, pady=5, bg="#0000ff")
but7 = Button(text="", width=20, pady=5, bg="#7d00ff")
lab = Label()


but1.bind("<Button-1>", showColor)
but2.bind("<Button-1>", showColor)
but3.bind("<Button-1>", showColor)
but4.bind("<Button-1>", showColor)
but5.bind("<Button-1>", showColor)
but6.bind("<Button-1>", showColor)
but7.bind("<Button-1>", showColor)


lab.pack()
color_abc.pack()
but1.pack()
but2.pack()
but3.pack()
but4.pack()
but5.pack()
but6.pack()
but7.pack()


root.mainloop()
