from tkinter import*
import time
from tkinter import messagebox

screen = Tk()

screen.geometry("300x250")
screen.config(background= "grey")

hour = StringVar()
minute = StringVar()
second = StringVar()
hour.set("00")
minute.set("00")
second.set("00")
hour_entry = Entry(screen,textvariable=hour,width=5)
hour_entry.place(x=50,y=30)
minute_entry = Entry(screen,textvariable=minute,width= 5)
minute_entry.place(x=100,y=30) 

second_entry = Entry(screen,textvariable=second,width= 5)
second_entry.place(x=160,y= 30)

def timer():
    temp = int(hour_entry.get())*3600 + int(minute_entry.get())*60+int(second_entry.get())
    while(temp>-1):
        mins,secs = divmod(temp,60)
        hours = 00
        if mins>60:
            hours,mins = divmod(mins,60)
        hour.set("{00:2d}".format(hours))
        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))
        screen.update()
        time.sleep(1) 
        if temp == 00:
            messagebox.showinfo("TIMER","TIMES UP")
        temp-=1
start = Button(screen,text = "start the timer",command = timer)
start.place(x = 100,y = 200) 


        

        




mainloop()