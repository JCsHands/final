'''
Program: Whack-A-Mole
Author: Jacob Carlisle
Propose: Creates an amusing game of whack-a-mole
Variables:



Inputs:
Outputs:
'''

from multiprocessing.sharedctypes import Value
from breezypythongui import EasyFrame
import time
import random
from tkinter import PhotoImage
bgColor = "#6f4e37"
moleCounter = 0

LifeCounter = 3
class WhackAMole(EasyFrame):
    def __init__(self):
        
        EasyFrame.__init__(self, title = "Whack-A-Mole")
        self.setSize(700, 700)
        
        #Instructions
        self.addLabel(text = "Score:", row = 0, column = 0, sticky = "NSE")
        self.moleCount = self.addLabel(text = "0",row = 0, column = 1, sticky = "NSW")
        self.addButton(text = "New Game",row = 0, column = 2, command = self.newGame)
        self.addButton(text = "High Score",row = 0, column = 3, command = self.highScoreWindow)
        self.addButton(text = "End Game", row = 0, column = 4, command = self.endGame)
        self.addPanel(row = 0, column = 5, background = "white")
        self.addPanel(row = 1, column = 0, background = bgColor)
        self.addPanel(row = 1, column = 1, background = bgColor)
        self.addPanel(row = 1, column = 2, background = bgColor)
        self.addPanel(row = 1, column = 3, background = bgColor)
        self.addPanel(row = 1, column = 4, background = bgColor)
        self.addPanel(row = 1, column = 5, background = bgColor)
        self.addPanel(row = 2, column = 0, background = bgColor)
        self.addPanel(row = 2, column = 1, background = bgColor)
        self.addPanel(row = 2, column = 2, background = bgColor)
        self.addPanel(row = 2, column = 3, background = bgColor)
        self.addPanel(row = 2, column = 4, background = bgColor)
        self.addPanel(row = 2, column = 5, background = bgColor)
        self.addPanel(row = 3, column = 0, background = bgColor)
        self.addPanel(row = 3, column = 1, background = bgColor)
        self.addPanel(row = 3, column = 2, background = bgColor)
        self.addPanel(row = 3, column = 3, background = bgColor)
        self.addPanel(row = 3, column = 4, background = bgColor)
        self.addPanel(row = 3, column = 5, background = bgColor)
        self.addPanel(row = 4, column = 0, background = bgColor)
        self.addPanel(row = 4, column = 1, background = bgColor)
        self.addPanel(row = 4, column = 2, background = bgColor)
        self.addPanel(row = 4, column = 3, background = bgColor)
        self.addPanel(row = 4, column = 4, background = bgColor)
        self.addPanel(row = 4, column = 5, background = bgColor)
        self.addPanel(row = 5, column = 0, background = bgColor)
        self.addPanel(row = 5, column = 1, background = bgColor)
        self.addPanel(row = 5, column = 2, background = bgColor)
        self.addPanel(row = 5, column = 3, background = bgColor)
        self.addPanel(row = 5, column = 4, background = bgColor)
        self.addPanel(row = 5, column = 5, background = bgColor)

        self.mole = self.addButton(text = "", row = 3, column = 2, command = self.moleMover)
        self.image = PhotoImage(file = "mole.gif")
        self.mole["image"] = self.image
        #self.countdown()


    def moleMover(self):
        global moleCounter
        moleCounter = 0
        r = random.randint(1, 5)
        c = random.randint(1, 5)
        self.mole.grid(row = r, column = c)
        moleCounter += 1
        self.moleCount["text"] = moleCounter

    def countdown(self):
        while 5:
            divmod(5, 60)
            time.sleep(1)
            5 - 1
        self.moleMover

    def endGame(self):
        playerName = self.prompterBox(title = "Players Name", promptString = "Enter your name:")
        playerScore = (playerName + " " + str(moleCounter) + "\n")
        f = open("scores.txt", 'a')
        f.write(playerScore)
        f.close()

    def newGame(self):
        self.mole.grid(row = 3, column = 3)
        moleCounter = 0
    
    def highScoreWindow(self):
        EasyFrame.highScoreWindow(self, title = "High Score")
        self.setSize(700, 700)
        self.addLabel(text = "Score:", row = 0, column = 0, sticky = "NSE")
        self.moleCount = self.addLabel(text = "0",row = 0, column = 1, sticky = "NSW")
        self.addButton(text = "New Game",row = 0, column = 2, command = self.newGame)
        self.addButton(text = "High Score",row = 0, column = 3)
        self.addButton(text = "End Game", row = 0, column = 4, command = self.endGame)

        
        #Instructions
        self.addLabel(text = "Score:", row = 0, column = 0, sticky = "NSE")
        self.moleCount = self.addLabel(text = "0",row = 0, column = 1, sticky = "NSW")
        self.addButton(text = "New Game",row = 0, column = 2, command = self.newGame)
        self.addButton(text = "High Score",row = 0, column = 3)
        self.addButton(text = "End Game", row = 0, column = 4, command = self.endGame)
        self.addPanel(row = 0, column = 5, background = "white")

def main():
    WhackAMole().mainloop()

if __name__ == "__main__":
    main()