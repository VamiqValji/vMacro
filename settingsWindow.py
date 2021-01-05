from tkinter import *
import os
from os import listdir
from os.path import isfile, join
from defaultSettings import importDefaultSettings
from defaultSettings import getColor


def openSettingsWindow():

    logsFolder = os.path.dirname(os.path.abspath(
        __file__)) + f"/logs/"

    def empty(padY=1, txt=""):
        return Label(text=txt, pady=padY, bg=bgColor, fg=textColor).pack()

    def saveChanges(theme):
        f = open(os.path.join(logsFolder, "settings.txt"), "w")
        if theme == "Default":
            f.write("Default")
        elif theme == "Dark":
            f.write("Dark")
        f.close()

    root = Tk()
    bgColor = getColor("bg")
    textColor = getColor("text")
    importDefaultSettings(root)

    Label(root, text="Settings", bg=bgColor, fg=textColor).pack()

    themeDropDown = StringVar()
    themeDropDown.set("Default")

    empty()
    OptionMenu(
        root, themeDropDown, *["Default", "Dark"]).pack()
    empty()
    Button(
        root, text="Save Changes", padx=10, pady=5, command=lambda: saveChanges(themeDropDown.get()), bg=bgColor, fg=textColor).pack()
    empty()
    updateTextChanges1 = Label(
        root, text="To see your changes in action,", bg=bgColor, fg=textColor, padx=5)
    updateTextChanges2 = Label(
        root, text="you may need to re-open the window.", bg=bgColor, fg=textColor, padx=5)
    updateTextChanges1.pack()
    updateTextChanges2.pack()
    empty(0.1)

    mainloop()


openSettingsWindow()
