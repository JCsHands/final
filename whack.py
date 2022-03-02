'''
Program: Whack-A-Mole
Author: Jacob Carlisle
Propose: Creates an amusing game of whack-a-mole
Variables:



Inputs:
Outputs:
'''

from breezypythongui import EasyFrame
import time
import random

class WhackAMole(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Whack-A-Mole")
        self.setSize(600, 600)
        #Instructions
        self.addLabel(text = "(0, 0)", row = 0, column = 0)
        self.addLabel(text = "(0, 1)", row = 0, column = 1)
        self.addLabel(text = "(0, 2)", row = 0, column = 2)
        self.addLabel(text = "(0, 3)", row = 0, column = 3)
        self.addLabel(text = "(0, 4)", row = 0, column = 4)
        self.addLabel(text = "(1, 0)", row = 1, column = 0)
        self.addLabel(text = "(1, 1)", row = 1, column = 1)
        self.addLabel(text = "(1, 2)", row = 1, column = 2)
        self.addLabel(text = "(1, 3)", row = 1, column = 3)
        self.addLabel(text = "(1, 4)", row = 1, column = 4)
        self.addLabel(text = "(2, 0)", row = 2, column = 0)
        self.addLabel(text = "(2, 1)", row = 2, column = 1)
        self.addLabel(text = "(2, 2)", row = 2, column = 2)
        self.addLabel(text = "(2, 3)", row = 2, column = 3)
        self.addLabel(text = "(2, 4)", row = 2, column = 4)
        self.addLabel(text = "(3, 0)", row = 3, column = 0)
        self.addLabel(text = "(3, 1)", row = 3, column = 1)
        self.addLabel(text = "(3, 2)", row = 3, column = 2)
        self.addLabel(text = "(3, 3)", row = 3, column = 3)
        self.addLabel(text = "(3, 4)", row = 3, column = 4)
        self.addLabel(text = "(4, 0)", row = 4, column = 0)
        self.addLabel(text = "(4, 1)", row = 4, column = 1)
        self.addLabel(text = "(4, 2)", row = 4, column = 2)
        self.addLabel(text = "(4, 3)", row = 4, column = 3)
        self.addLabel(text = "(4, 4)", row = 4, column = 4)
        self.mole = self.addButton(text = "Mole", row = 2, column = 2, command = self.moleMover)
        #self.countdown()


    def moleMover(self):
            r = random.randint(0, 3)
            c = random.randint(0, 3)
            self.mole.grid(row = r, column = c)
    
    def countdown(self):
        while 5:
            divmod(5, 60)
            time.sleep(1)
            5 - 1
        self.moleMover

def main():
    WhackAMole().mainloop()

if __name__ == "__main__":
    main()