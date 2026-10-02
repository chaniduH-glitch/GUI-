from tkinter import* 
from tkinter.ttk import* 
from time import strftime 

screen = Tk()
screen.geometry("600x400")
screen.title("clock") 
def display_time():
    string = strftime("%H:%M:%S %p")
    time.config(text = string)
    time.after(1000,display_time)

time = Label(screen,background= "grey",foreground="black", font = ("Arial",30)) 

time.place(x=35,y=70)
display_time()   

mainloop() 

