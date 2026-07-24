from tkinter import* 
from tkinter.ttk import*
import time
screen = Tk()
screen.title("progress bar")
screen.geometry("200x300")
screen.config(background = "red")

user_progress = Progressbar(screen,orient=HORIZONTAL,length = 100)
def bar():
    user_progress["value"] = 20
    screen.update_idletasks()
    time.sleep(1)
    user_progress["value"]=40
    screen.update_idletasks()
    time.sleep(1)
    user_progress["value"] = 60 
    screen.update_idletasks()
    time.sleep(1)
    user_progress["value"] = 80
    screen.update_idletasks()
    time.sleep(1)
    user_progress["value"] = 100
user_progress.place(x=40,y=90)
    
progress_button = Button(screen,text = "start",command=bar).place(x=45,y=140)


mainloop()




