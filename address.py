from tkinter import*
from tkinter import messagebox
screen = Tk()
screen.geometry("500x600")
screen.config(background="red")

dict1 = {}
def display(event):
    new_window = Toplevel(screen)
    index = listbox1.curselection()
    contact = ""
    if index:
        key = listbox1.get(index) 
        contact = "Name :"+key+"\n"
        details = dict1[key]
        contact+="address :"+details[0]+"\n"
        contact+="mobile :"+details[1]+"\n"
        contact+="email :"+details[2]+"\n"
        contact+="birthday :"+details[3]+"\n"
        l = Label(new_window)
        l.place(x=10,y=10)
        l.configure(text=contact)


def add(): 
    key = name_enter.get()
    if key == "":
        messagebox.showinfo("name","name cannot be empty")
    else:
        if key not in dict1.keys():
            listbox1.insert(END,key)
        dict1[key] = (address_enter.get(),mobile_enter.get(),email_enter.get(),birthday_enter.get())
        clear_all()



    

    


def clear_all():
    name_enter.delete(0,END)
    address_enter.delete(0,END)
    mobile_enter.delete(0,END)
    email_enter.delete(0,END)
    birthday_enter.delete(0,END)



def edit():
    clear_all()
    selecteditems = listbox1.curselection()
    if selecteditems:
        name_enter.insert(0,listbox1.get(selecteditems))
        details = dict1[name_enter.get()]
        address_enter.insert(0,details[0])
        mobile_enter.insert(0,details[1])
        email_enter.insert(0,details[2])
        birthday_enter.insert(0,details[3])
    else: 
        messagebox.showinfo("error","select a name")


address_name = Label(screen,text="my address book")
address_name.place(x=130,y=50)
name = Label(screen,text = "name")
name.place(x=250,y=100)

address = Label(screen,text ="Address")
address.place(x=250,y=130)

mobile = Label(screen,text="mobile")
mobile.place(x=250,y=160)

email = Label(screen,text = "email")
email.place(x=250,y=190)

birthday = Label(screen,text="birthday")
birthday.place(x=250,y=220)

name_enter = Entry(screen,width=15)
name_enter.place(x=320,y=100)

address_enter = Entry(screen,width= 15)
address_enter.place(x=320,y=130)

mobile_enter = Entry(screen,width = 15)
mobile_enter.place(x=320,y=160)

email_enter = Entry(screen,width = 15)
email_enter.place(x=320,y=190)

birthday_enter = Entry(screen,width=15)
birthday_enter.place(x=320,y=220)

open = Button(screen,text="open")
open.place(x=250,y=50)

listbox1 = Listbox(screen,width=30)
listbox1.place(x=50,y=100)
listbox1.bind("<<ListboxSelect>>",display)



edit1 = Button(screen,text="edit",command = edit)
edit1.place(x=50,y=280)

delete = Button(screen,text="delete")
delete.place(x=85,y=280)

update_add = Button(screen,text="update/add",command = add)
update_add.place(x=350,y=280)

save = Button(screen,text="save",width=25)
save.place(x=150,y=320)












mainloop()
