from tkinter import*
from tkinter.ttk import*
screen = Tk()

screen.geometry("300x400")
screen.config(background="grey")
math_table = Label(screen,text="multiplications table")
math_table.place(x=100,y=20)
numbers_range = Label(screen,text="numbers and range")
numbers_range.place(x=15,y=50)
num = IntVar()
combobox = Combobox(screen,textvariable=num,width = 7)
combobox["values"]=list(range(0,101))
combobox.place(x=130,y = 50)
radiobutton = IntVar()
radiobutton10 = Radiobutton(screen,text="10",variable=radiobutton,value = 10)
radiobutton20 = Radiobutton(screen,text="20",variable=radiobutton,value=20)
radiobutton30 = Radiobutton(screen,text="30",variable = radiobutton,value=30)
radiobutton.set(10)
radiobutton10.place(x=230,y=50)
radiobutton20.place(x=230,y=70)
radiobutton30.place(x=230,y=90)






mainloop()

