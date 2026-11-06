from tkinter import*
screen = Tk()
screen.geometry("500x600")
screen.config(background="red")

name = Label(screen,text = "name")
name.place(x=250,y=100)

address = Label(screen,text ="Address")
address.place(x=250,y=130)

mobile = Label(screen,text="mobile")
mobile.place(x=250,y=160)

email = Label(screen,text = "email")
email.place(x=250,y=190)

birthday = Label(screen,text="birthday")
birthday.place(x=250,y=220)

name_enter = Entry(screen,width=15)
name_enter.place(x=320,y=100)

address_enter = Entry(screen,width= 15)
address_enter.place(x=320,y=130)






mainloop()
