from tkinter import *
screen = Tk()
screen.title("Book Inventory") 
screen.geometry("400x600")
screen.config(background="red") 

enter_book = Label(screen,text = "book title").place(x=40,y=50)
enter_author = Label(screen,text = "author").place(x=40,y=90)
enter_price = Label(screen,text = "price").place(x=40,y=130) 
book_title = Entry(screen,width=20).place(x=100,y=50)
author = Entry(screen,width=20).place(x=85,y=90)
price = Entry(screen,width=20).place(x=85,y=130)
save_book = Button(screen,text="save").place(x=110,y=170)

mainloop()



 