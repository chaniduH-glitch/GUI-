from tkinter import *

screen = Tk()

screen.title("Area Calculator")
screen.geometry("400x350")


length_value = StringVar()
width_value = StringVar()


length = Label(screen,text="Length")
length.place(x=30,y=50)

enter_length = Entry(screen,width=20,textvariable=length_value)
enter_length.place(x=110,y=50)


width = Label(screen,text="Width")
width.place(x=30,y=100)

enter_width = Entry(screen,width=20,textvariable=width_value)
enter_width.place(x=110,y=100)


def calculate():
    length = float(length_value.get())
    width = float(width_value.get())
    area = length * width
    result.config(text="Area: " + str(area) + " sq units")


calculate_button = Button(screen,text="Calculate Area",command=calculate)
calculate_button.place(x=110,y=150)


result = Label(screen,text="")
result.place(x=45,y=220)


mainloop()