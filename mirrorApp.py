from tkinter import *

screen = Tk()

screen.title("Mirror App")
screen.geometry("400x300")
screen.config(background="white")


entry = Entry(screen,width=25)
entry.place(x=120,y=50)


def copy_text():
    value = entry.get()
    label.config(text=value)


button = Button(screen,text="Copy Text",command=copy_text)
button.place(x=160,y=100)


label = Label(screen,text="")
label.place(x=150,y=180)


mainloop()