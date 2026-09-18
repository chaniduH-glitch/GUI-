from tkinter import *

screen = Tk()


screen.title("Currency Converter")
screen.geometry("500x400")
screen.config(background="white")


value = StringVar()

usd = Label(screen,text="Enter USD ($):")
usd.place(x=40,y=80)

enter = Entry(screen,width=25,textvariable=value)
enter.place(x=170,y=80)


def convert():
    dollars = float(value.get())
    rupees = dollars * 83
    result.delete("1.0",END)
    result.insert(END,rupees)

    

  


convert_button = Button(screen,text="Convert to INR",command=convert)
convert_button.place(x=170,y=130)


answer = Label(screen,text="Result in INR:")
answer.place(x=40,y=200)

result = Text(screen,width = 5, height =1)
result.place(x=170,y=200) 


mainloop()