from tkinter import * 
screen = Tk ()
screen.title("listbox")
screen.geometry("400x600")
screen.config(background = "red")
list_store = Listbox(screen,width = 20, height = 30,bg = "grey")
list_store.insert(1,"burger")
list_store.insert(2,"rice")
list_store.insert(3,"pizza")
list_store.insert(4,"hotdog") 
list_store.place(x = 25, y= 35) 
mainloop()

