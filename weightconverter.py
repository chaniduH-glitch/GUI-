from tkinter import*
screen = Tk()
screen.geometry("400x600")
def calc():
    g = float(value.get())*1000 
    p = float(value.get())*2.20462 
    o = float(value.get())*35.274
    text1.delete("1.0",END)
    text2.delete("1.0",END)
    text3.delete("1.0",END)
    text1.insert(END,g)
    text2.insert(END,p)
    text3.insert(END,o) 





weight = Label(screen,text= "enter the weight in kg")
weight.place(x =140,y = 100)
value = StringVar()
enter = Entry(screen,width=25,textvariable=value)
enter.place(x=120,y= 120)
convert = Button(screen,text="convert", command= calc)
convert.place(x=160,y=140)
grams = Label(screen,text = "grams")
grams.place(x = 80,y=165)
pounds = Label(screen,text = "pounds")
pounds.place(x = 150,y =165 )
ounce = Label(screen,text = "ounces")
ounce.place(x = 220, y = 165)

text1 = Text(screen,width=5,height= 1)
text1.place(x =80, y=200 )

text2 = Text(screen,width=5,height=1)
text2.place(x = 150, y = 200)

text3 = Text(screen,width=5,height=1)
text3.place(x=220,y=200)



mainloop()  
