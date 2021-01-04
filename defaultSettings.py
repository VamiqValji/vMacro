from tkinter import *
import os
from os import listdir
from os.path import isfile, join


def importDefaultSettings():
    thisFolder = os.path.dirname(os.path.abspath(
        __file__)) + f"/img/"
    img = os.path.join(thisFolder, "vMacroLogo.ico")

    root = Tk()
    root.title("vMacro")
    root.iconbitmap(img)

    root.configure(bg="black")

# Label(text="Default Window Settings").pack()

# mainloop()
