from tkinter import * 
screen = Tk ()
screen.title("listbox")
screen.geometry("400x600")
screen.config(background = "red")
label = Label(screen,text= "calandar",bg = "grey",font=("arial",30,"bold"))
label.place(x =90, y = 50)
year = Label(screen,text = "enter the year")
year.place(x = 130,y = 150)
entrybox = Entry(screen)
entrybox.place(x = 110,y =200)

mainloop()

