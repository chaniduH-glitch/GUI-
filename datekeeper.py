
from tkinter import *
import time

screen = Tk()
screen.title("Calendar Widget")
screen.geometry("400x200")
screen.config(background="lightblue")

def date():
    today = time.strftime("%B %d, %Y")
    date_label.config(text=today)

date_label = Label(screen, text="", font=("Arial", 20), bg="lightblue")
date_label.place(x=70, y=80)

date()

screen.mainloop()

    