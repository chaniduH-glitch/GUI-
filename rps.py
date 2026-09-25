import random
from tkinter import*
screen = Tk()
screen.geometry("600x400")
screen.config(background="red")
player_score = 0
computer_score = 0

options = [("rock",0),("paper",1),("scissors",2)]
def computer_win():
    global computer_score,player_score
    computer_score +=1
    determiner.config(text = "COMPUTER WON!")
    playerscorel.config(text = "your score"+str(player_score))
    computerscorel.config(text = "computer score"+str(computer_score))

def player_win():
    global computer_score,player_score
    player_score +=1 
    determiner.config(text = "PLAYER WON!")
    playerscorel.config(text = "your score"+str(player_score))
    computerscorel.config(text = "computer score"+str(computer_score)) 

def tie():
    global computer_score,player_score
    determiner.config(text= "TIE!")
    playerscorel.config(text = "your score"+str(player_score))
    computerscorel.config(text = "computer score"+str(player_score))

def player_choice(playerinput):
    global player_score,computer_score
    computerinput = computer_choice()
    player_choicel.config(text = "you selected:"+playerinput[0])
    computerchoicel.config(text = "computer selected:"+computerinput[0])
    if playerinput == computerinput:
        tie()
    if playerinput[1]== 0:
        if computerinput[1]== 1:
            computer_win()
        elif computerinput[1]== 2:
            player_win()

    elif playerinput[1]== 1:
        if computerinput[1]== 0:
            player_win()
        elif computerinput[1]==2:
            computer_win()

    elif playerinput[1]== 2:
        if computerinput[1]== 1:
            player_win()
        elif computerinput[1]==0:
            computer_win() 
def computer_choice():
    return random.choice(options)   

                          



    
    


title = Label(screen,text = "Rock Paper Scissors")
title.place(x=240,y=50)

determiner = Label(screen,text = "Lets begin the game")
determiner.place(x = 240,y=100)
player_options = Label(screen,text= "your options")
player_options.place(x=100,y=140)
rockb = Button(screen,text="ROCK",command = lambda:player_choice(options[0]))
rockb.place(x=200,y=160)
paperb = Button(screen,text = "PAPER",command = lambda: player_choice(options[1]))
paperb.place(x=280,y= 160)
scissorsb = Button(screen,text="SCISSORS",command= lambda: player_choice(options[2]))
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
