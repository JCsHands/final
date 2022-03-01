from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter import font
import time

class LayoutDemo(EasyFrame):
    """Displays labels in the quadrants."""

    def __init__(self):
        """Sets up the window and the labels."""
        EasyFrame.__init__(self)
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
        self.addButton(text = "Here I am", row = 1, column = 0,)

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1   

def main():
    """Instantiate and pop up the window."""
    LayoutDemo().mainloop()
if __name__ == "__main__":
    main()

