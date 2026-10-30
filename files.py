from tkinter import*
from tkinter.filedialog import*

screen = Tk()
screen.geometry("400x600")
screen.title("files app")

save = Button(screen,text = "SAVE")
save.place(x=170,y=150)

delete = Button(screen,text = "DELETE")
delete.place(x=300,y=300)
open = Button(screen,text = "OPEN")
open.place(x=50,y=300)

add = Button(screen,text = "ADD")
add.place(x=170,y=500)
add_entry = Entry(screen,width=25)
add_entry.place(x=120,y=460)

scroll = Scrollbar(screen,orient="vertical")
scroll.pack(side= LEFT,fill=Y)

file_lists = Listbox(screen,width=20,yscrollcommand=scroll.set)
for i in range(100):
    file_lists.insert(END,"list"+str(i))
file_lists.pack(side= RIGHT,padx=5)
scroll.config(command=file_lists.yview)








mainloop()