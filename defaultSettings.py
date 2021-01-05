from tkinter import *
import os
from os import listdir
from os.path import isfile, join


global thisFolder
thisFolder = os.path.dirname(os.path.abspath(
    __file__))


# def returnSettings():
#     f = open(os.path.join(thisFolder, "logs/settings.txt"), "r")
#     settings = f.readlines()
#     f.close()
#     return settings

global settings

f = open(os.path.join(thisFolder, "logs/settings.txt"), "r")
settings = f.readlines()
f.close()


def returnColors():
    theme = settings[0]
    if theme == "Default":
        bgColor = "#ecf0f1"
        textColor = "black"
    elif theme == "Dark":
        bgColor = "#2c3e50"
        textColor = "#ecf0f1"
    elif theme == "Black":
        bgColor = "black"
        textColor = "white"
    if theme == "Bright":
        bgColor = "#fd79a8"
        textColor = "#2d3436"
    return[bgColor, textColor]


def importDefaultSettings(root):
    root.title("vMacro")
    root.iconbitmap(os.path.join(thisFolder, "img/vMacroLogo.ico"))

    bgCol = returnColors()[0]

    root.configure(bg=bgCol)


def getColor(RETURN):

    colorsList = returnColors()

    if RETURN == "bg":
        return colorsList[0]
    elif RETURN == "text":
        return colorsList[1]


# Label(text="Default Window Settings").pack()

# mainloop()
