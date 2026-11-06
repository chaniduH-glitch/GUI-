from tkinter import*
from tkinter.filedialog import*

screen = Tk()
screen.geometry("400x600")
screen.title("files app")


def delete_item():
    item = file_lists.curselection()
    if item:
        file_lists.delete(item)

def add_item():
    file_lists.insert(END,add_entry.get())
    add_entry.delete(0,END)

def save_file():
    f = asksaveasfile(defaultextension=".txt")
    if f is not None:
        for i in file_lists.get(0,END):
            print(i.strip(),file= f)
        file_lists.delete(0,END)

        


def open_file():
    f = askopenfile(title = "open file")
    if f is not None:
        file_lists.delete(0,END) 
        items = f.readlines()
        for i in items:
            file_lists.insert(END,i.strip())

save = Button(screen,text = "SAVE",command = save_file)
save.place(x=170,y=150,)

delete = Button(screen,text = "DELETE",command = delete_item)
delete.place(x=300,y=300)
open = Button(screen,text = "OPEN",command=open_file)
open.place(x=50,y=300)

add = Button(screen,text = "ADD",command = add_item)
add.place(x=170,y=500)
add_entry = Entry(screen,width=25)
add_entry.place(x=120,y=460)

scroll = Scrollbar(screen,orient="vertical")
scroll.place(x=250,y=200,height=150)

file_lists = Listbox(screen,width=20,yscrollcommand=scroll.set)
for i in range(100):
    file_lists.insert(END,"list"+str(i))
file_lists.place(x=130,y=200)


scroll.config(command=file_lists.yview)







mainloop()