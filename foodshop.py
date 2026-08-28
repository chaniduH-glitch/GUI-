from tkinter import *
from tkinter.ttk import *
import time

screen = Tk()

screen.title("Food Order")
screen.geometry("700x500")
screen.config(background="red")
# Email
email = Label(screen,text="Email")
email.place(x=155,y=40)
enter_email = Entry(screen,width=30)
enter_email.place(x=210,y=40)

# Password
password = Label(screen,text="Password")
password.place(x=130,y=80)
enter_password = Entry(screen,width=30,show="*")
enter_password.place(x=210,y=80)

# Food
food = Label(screen,text="What food would you like: Chicken sandwich, B.L.T, Veg sandwich? or None")
food.place(x=100,y=150)

food_entry = Entry(screen,width=25)
food_entry.place(x=90,y=175)

food_spinbox = Spinbox(screen,from_=0,to=10)
food_spinbox.place(x=360,y=175)


# Beverage
beverage = Label(screen,text="What beverage would you like: Cola, Fanta, Orange Juice, Water or None?")
beverage.place(x=105,y=220)

beverage_entry = Entry(screen,width=25)
beverage_entry.place(x=90,y=245)

beverage_spinbox = Spinbox(screen,from_=0,to=10)
beverage_spinbox.place(x=360,y=245)


# Dessert
dessert = Label(screen,text="What dessert would you like: An Ice Cream, an Ice Lolly or a Chocolate Cake or None?")
dessert.place(x=90,y=290)

dessert_entry = Entry(screen,width=25)
dessert_entry.place(x=90,y=315)

dessert_spinbox = Spinbox(screen,from_=0,to=10)
dessert_spinbox.place(x=360,y=315)



# Progress bar
progress = Progressbar(screen,orient=HORIZONTAL,length=180)
def bar():
    progress["value"] = 20
    screen.update_idletasks()
    time.sleep(1)
    progress["value"]=40
    screen.update_idletasks()
    time.sleep(1)
    progress["value"] = 60 
    screen.update_idletasks()
    time.sleep(1)
    progress["value"] = 80
    screen.update_idletasks()
    time.sleep(1)
    progress["value"] = 100
progress.place(x=230,y=410)

submit = Button(screen,text="Submit Order",command = bar)
submit.place(x=275,y=375)



mainloop()