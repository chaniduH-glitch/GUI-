from tkinter import *
import calendar 
screen = Tk ()
screen.title("listbox")
screen.geometry("400x600")
screen.config(background = "red")
def display_cal():
    screen2 = Tk ()
    screen2.geometry("600x600")
    screen2.config(background = "white")
    year = int(entrybox.get())
    content = calendar.calendar(year)
    calendar_contents = Label(screen2,text = content)
    calendar_contents.place(x = 10,y = 10)




label = Label(screen,text= "calandar",bg = "grey",font=("arial",30,"bold"))
label.place(x =90, y = 50)
year = Label(screen,text = "enter the year")
year.place(x = 130,y = 150)
entrybox = Entry(screen)
entrybox.place(x = 110,y =200)
show_calendar = Button(screen,text = "show calendar",command=display_cal)
show_calendar.place(x=125, y = 230)
exit = Button(screen,text = "Exit",command = screen.destroy) 
exit.place(x = 150,y = 290) 
mainloop()  

