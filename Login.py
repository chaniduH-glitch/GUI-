from tkinter import*
screen = Tk()
screen.title("Login") 
screen.geometry("400x600")
screen.config(background="red")
user = Label(screen,text = "username").place(x=40,y=50)
user_password = Label(screen,text = "password").place(x=40,y=90)
enter_name = Entry(screen,width=20).place(x=100,y=50)
password = Entry(screen,width=20,show= "*").place(x=100,y=90)
submit = Button(screen,text="submit",command = screen.destroy).place(x=110,y=120)


mainloop()


