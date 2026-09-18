from tkinter import*
screen = Tk()
screen.geometry("600x400")
screen.config(background="red")

title = Label(screen,text = "Rock Paper Scissors")
title.place(x=240,y=50)

determiner = Label(screen,text = "Lets begin the game")
determiner.place(x = 240,y=100)
player_options = Label(screen,text= "your options")
player_options.place(x=100,y=140)
rockb = Button(screen,text="ROCK")
rockb.place(x=200,y=160)
paperb = Button(screen,text = "PAPER")
paperb.place(x=280,y= 160)
scissorsb = Button(screen,text="SCISSORS")
scissorsb.place(x=360,y=160)
player_choicel = Label(screen,text="you selected:")
player_choicel.place(x=200,y= 250)
computerchoicel = Label(screen,text="computer selected:")
computerchoicel.place(x = 200, y= 300) 
scorel = Label(screen,text = "SCORE")
scorel.place(x=100,y=230)
playerscorel = Label(screen,text="your score")
playerscorel.place(x=400,y=250)
computerscorel = Label(screen,text="computer score")
computerscorel.place(x=400,y=300)





mainloop()
