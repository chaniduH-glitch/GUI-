
from tkinter import *

screen = Tk()
screen.title("Pizza App")
screen.geometry("720x320")
screen.config(background="red")

# Welcome label
title = Label(screen, text="Welcome to Pizza Hut", bg="white")
title.place(x=290, y=65)

# Pizza selection
pizza_label = Label(screen, text="Select Your Fav Pizza:", bg="white")
pizza_label.place(x=20, y=125)

pizza_choice = StringVar()
pizza_choice.set("Veg Extravaganza")

pizza_menu = OptionMenu(screen, pizza_choice, "Veg Extravaganza", "Margherita", "Farmhouse")
pizza_menu.place(x=295, y=115)

# Quantity selection
quantity_label = Label(screen, text="Enter Quantity:", bg="white")
quantity_label.place(x=40, y=165)

quantity_choice = StringVar()
quantity_choice.set("1")

quantity_menu = OptionMenu(screen, quantity_choice, "1", "2", "3", "4", "5", "6", "7")
quantity_menu.place(x=295, y=155)

# Pizza size
pizza_size = StringVar()
pizza_size.set("S")

small = Radiobutton(screen, text="S", variable=pizza_size, value="Small", bg="white")
small.place(x=640, y=125)

medium = Radiobutton(screen, text="M", variable=pizza_size, value="Medium", bg="white")
medium.place(x=640, y=165)

large = Radiobutton(screen, text="L", variable=pizza_size, value="Large", bg="white")
large.place(x=640, y=205)

# Order function
def order():
    pizza = pizza_choice.get()
    quantity = quantity_choice.get()
    size = pizza_size.get()

    result.config(text="You ordered " + quantity + " " + pizza + " " + size + " Size Pizza(s)")

# Order button
order_button = Button(screen, text="Order", command=order)
order_button.place(x=340, y=240)

# Confirmation label
result = Label(screen, text="", bg="white")
result.place(x=210, y=280)

screen.mainloop()

