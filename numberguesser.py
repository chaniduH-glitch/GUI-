from tkinter import*
import tkinter.messagebox
import random 

screen = Tk()
screen.geometry("600x400")
screen.config(background = "grey")
def message():
    my_name = name_entry.get()
    tkinter.messagebox.showinfo("name","hello "+ my_name+" I am thinking of a number between 1-20")
n = random.randint(1,20)
def guessing():
    num = number.get()
    num = int(num)
    if num > n:
        tkinter.messagebox.showinfo("high","your number is too high")
    elif n > num:
        tkinter.messagebox.showinfo("low","your number is too low")
    elif n == num:
        tkinter.messagebox.showinfo("correct","you guessed the number!")



welcome = Label(screen,text = "welcome to the game")
welcome.place(x = 250,y = 100) 
name = Label(screen,text = "enter your name")
name.place(x = 100, y = 150)
name_entry = Entry(screen,width=25)
name_entry.place(x = 100, y = 180)
okbutton = Button(screen,text = "OK",command = message)

okbutton.place(x = 400, y = 165)
guess = Label(screen,text = "guess a number")
guess.place(x = 100, y = 230)
number = Entry(screen,width = 25)
number.place(x = 100, y =260) 
confirm = Button(screen,text = "confirm",command = guessing)
confirm.place(x = 400,y = 245)

mainloop()
