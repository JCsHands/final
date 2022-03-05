'''
Program: Whack-A-Mole
Author: Jacob Carlisle
Propose: Creates an amusing game of whack-a-mole
Variables:
moleCounter
LifeCounter

Inputs:
Outputs: users scores are stored in a scores.txt file.
'''


import time
import random
from tkinter import *
from tkinter import messagebox
moleCounter = 0
LifeCounter = 3

WaM = Tk()
WaM.title("Whack-a-Mole")
WaM.iconbitmap("mole.ico")
WaM.geometry("880x620")
moleImg = PhotoImage(file='mole.gif')
yardImg = PhotoImage(file='yard.gif')

def moleMover():
    '''Moves the mole around by randomly generating his row and column'''
        global moleCounter
        r = random.randint(1, 5)
        c = random.randint(0, 5)
        mole.grid(row = r, column = c)
        scoreKeeper()

def scoreKeeper():
    '''Increments and displays the moleCounter var (Players Score)'''
    global moleCounter
    moleCounter += 1
    print(moleCounter)
    heading01.config(text = moleCounter)

def wrongBox():
    '''Decrements and displays the LifeCounter var (players Lives)'''
    global LifeCounter
    LifeCounter -= 1
    heading06.config(text = LifeCounter)
    print(LifeCounter)
    if LifeCounter == 0:
        endGame()

def endGame():
    '''Disables the mole and launches the High Score window'''
    mole['state'] = DISABLED
    highScoreWindow()


def newGame():
    '''Resets the moleCounter & LifeCounter vars and places the "mole" in the middle'''
    mole.grid(row = 3, column = 3)
    moleCounter = 0
    LifeCounter = 3

#    ---   High Score Window    ---   

def highScoreWindow():
    '''Launches the High Score window'''
   WaMHS = Tk()
   WaMHS.title("Whack-a-Mole Leader Board")
   WaMHS.iconbitmap("mole.ico")
   WaMHS.geometry("400x360")

   def recordScore():
       '''Writes the users entered name and score to the scores.txt file'''
      global playerName
      playerName = nameInput.get()
      playerScore = (playerName + " " + str(moleCounter) + "\n")
      f = open("scores.txt", 'a')
      f.write(playerScore)
      f.close()
      print(playerName + " " + str(moleCounter))

   def displayScores():
       '''Displays the content of the scores.txt file'''
       f = open('scores.txt', 'r')
       topScores = f.read()
       scores.insert('end', topScores)
       f.close()



#Widgets
   Banner = Label(WaMHS, text="High Scores")
   nameInput = Entry(WaMHS)
   submitName = Button(WaMHS, text="Enter Your Name", command=recordScore)
   scores = Text(WaMHS, width=40, height=20)

   
#Layout
   Banner.pack()
   nameInput.pack()
   submitName.pack()
   scores.pack()

    
    
#    ^--   End High Score Window     --^   


#    ----   Heading   ----
#Widgets
heading00 = Label(WaM, text="Score:")
heading01 = Label(WaM, text=moleCounter)
heading02 = Button(WaM, text="New Game", command = newGame)
heading03 = Button(WaM, text="High Scores", command = highScoreWindow)
heading04 = Button(WaM, text="End Game")
heading05 = Label(WaM, text="Lives Left:")
heading06 = Label(WaM, text=LifeCounter)



#Layout
heading00.grid(row=0, column=0)
heading01.grid(row=0, column=1)
heading02.grid(row=0, column=2)
heading03.grid(row=0, column=3)
heading04.grid(row=0, column=4)
heading05.grid(row=0, column=5)
heading06.grid(row=0, column=6)

#    ^---   End Heading   --^



#    ----   Yard   ----
#Widgets
yard1 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard2 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard3 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard4 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard5 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard6 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard7 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard8 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard9 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard10 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard11 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard12 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard13 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard14 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard15 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard16 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard17 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard18 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard19 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard20 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard21 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard22 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard23 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard24 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard25 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard26 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard27 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard28 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard29 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard30 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard31 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard32 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard33 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard34 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)
yard35 = Button(WaM, image=yardImg, command=wrongBox, state = NORMAL)


#Layout
yard1.grid(row=1, column=1)
yard2.grid(row=1, column=3)
yard3.grid(row=1, column=2)
yard4.grid(row=1, column=4)
yard5.grid(row=1, column=5)
yard6.grid(row=1, column=0)
yard7.grid(row=1, column=6)
yard8.grid(row=2, column=0)
yard9.grid(row=2, column=1)
yard10.grid(row=2, column=2)
yard11.grid(row=2, column=3)
yard12.grid(row=2, column=4)
yard13.grid(row=2, column=5)
yard14.grid(row=2, column=6)
yard15.grid(row=3, column=0)
yard16.grid(row=3, column=1)
yard17.grid(row=3, column=2)
yard18.grid(row=3, column=3)
yard19.grid(row=3, column=4)
yard20.grid(row=3, column=5)
yard21.grid(row=3, column=6)
yard22.grid(row=4, column=0)
yard23.grid(row=4, column=1)
yard24.grid(row=4, column=2)
yard25.grid(row=4, column=3)
yard26.grid(row=4, column=4)
yard27.grid(row=4, column=5)
yard28.grid(row=4, column=6)
yard29.grid(row=5, column=0)
yard30.grid(row=5, column=1)
yard31.grid(row=5, column=2)
yard32.grid(row=5, column=3)
yard33.grid(row=5, column=4)
yard34.grid(row=5, column=5)
yard35.grid(row=5, column=6)

#    ^---   End Yard   ---^

mole = Button(WaM, image=moleImg, command=moleMover)
mole.grid(row=3, column=3)

WaM.mainloop()