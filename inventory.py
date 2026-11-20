from tkinter import*
from tkinter.ttk import*
screen = Tk()
screen.config(background="light grey")
screen.geometry("800x1000")
smart_inventory = Label(screen,text="SMART INVENTORY MANAGER")
smart_inventory.place(x=130,y=65)
productname = Label(screen,text="Product Name:")
productname.place(x=80,y=100)

productname_entry = Entry(screen,width=25)
productname_entry.place(x=200,y=100)

product_id = Label(screen,text="Enter Product ID:")
product_id.place(x=80,y=150)

product_id_entry = Entry(screen,width =25)
product_id_entry.place(x=200,y=150)


price = Label(screen,text="Price($):")
price.place(x=80,y=200)

price_entry = Entry(screen,width=25)
price_entry.place(x=200,y=200)

quantity = Label(screen,text="Quantity:")
quantity.place(x=80,y=250)

quantity_entry = Entry(screen,width=25)
quantity_entry.place(x=200,y=250) 

listbox1 = Listbox(screen,width=30)
listbox1.place(x=400,y=100)

add_item = Button(screen,text="ADD ITEM")
add_item.place(x=80,y=320)

delete = Button(screen,text="DELETE")
delete.place(x=180,y=320)

clear = Button(screen,text="CLEAR")
clear.place(x=280,y=320)













mainloop()

