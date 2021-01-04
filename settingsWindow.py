from tkinter import *
import os
from os import listdir
from os.path import isfile, join
from defaultSettings import importDefaultSettings


def openSettingsWindow():

    logsFolder = os.path.dirname(os.path.abspath(
        __file__)) + f"/logs/"

    def empty(padY=1, txt=""):
        return Label(text=txt, pady=padY).pack()

    def saveChanges(theme):
        f = open(os.path.join(logsFolder, "settings.txt"), "w")
        if theme == "Default":
            f.write("Default")
        elif theme == "Dark":
            f.write("Dark")
        f.close()

    root = Tk()
    importDefaultSettings(root)

    Label(root, text="Settings").pack()

    themeDropDown = StringVar()
    themeDropDown.set("Default")

    empty()
    OptionMenu(
        root, themeDropDown, *["Default", "Dark"]).pack()
    empty()
    Button(
        root, text="Save Changes", padx=10, pady=5, command=lambda: saveChanges(themeDropDown.get())).pack()
    empty()

    mainloop()


# openSettingsWindow()
