from tkinter import*
screen = Tk()
screen.title("frame")
screen.geometry("400x600")
frame = Frame(screen,bg = "black",width = 200, height = 300).place(x=40,y=110)

button1 = Button(frame,text = "open").place(x=60,y=130)
button2 = Button(frame,text = "close",command=screen.destroy).place(x=60,y=170)

mainloop()