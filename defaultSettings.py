from tkinter import *
import os
from os import listdir
from os.path import isfile, join


def importDefaultSettings(root):
    thisFolder = os.path.dirname(os.path.abspath(
        __file__))

    root.title("vMacro")
    # root.iconbitmap(os.path.join(thisFolder, "/img/vMacroLogo.ico"))

    f = open(os.path.join(thisFolder, "logs/settings.txt"), "r")
    settings = f.readlines()
    f.close()

    bgColor = ""

    theme = settings[0]

    if theme == "Default":
        bgColor = ""
    if theme == "Dark":
        bgColor = "black"

    root.configure(bg=bgColor)

# Label(text="Default Window Settings").pack()

# mainloop()
