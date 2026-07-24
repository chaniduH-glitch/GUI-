from tkinter import*
screen = Tk()
screen.title("spin box")
screen.geometry("400x600")
screen.config(background ="red")

spinbox = Spinbox(screen,from_ = 4,to=20).place(x=40,y=110)


mainloop()
