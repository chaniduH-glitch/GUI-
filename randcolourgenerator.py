from tkinter import *
import random

screen = Tk()

screen.title("Color Magic")
screen.geometry("400x300")

colors = ["red", "blue", "green", "yellow", "purple", "orange"]


def change_color():
    random_color = random.choice(colors)
    screen.config(bg=random_color)
    label.config(text="Color is: " + random_color)


label = Label(screen,text="")
label.place(x=150,y=70)

button = Button(screen,text="Change Color",command=change_color)
button.place(x=150,y=130)

mainloop()