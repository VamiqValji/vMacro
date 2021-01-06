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
        f.write(theme)
        f.close()

    root = Tk()
    bgColor = getColor("bg")
    textColor = getColor("text")
    importDefaultSettings(root)

    Label(root, text="Settings", bg=bgColor, fg=textColor,
          font=("Helvetica", 18, "bold")).pack()
    # Label(root, text="", pady=1, bg=bgColor, fg=textColor).pack()

    Label(root, text="Theme", bg=bgColor,
          fg=textColor, font=("Helvetica", 11)).pack()
    themeDropDown = StringVar()
    themeDropDown.set("Default")

    # empty()
    OptionMenu(
        root, themeDropDown, *["Default", "Dark", "Black", "Bright"]).pack()
    # empty()
    Button(
        root, text="Save Changes", padx=10, pady=5, command=lambda: saveChanges(themeDropDown.get()), bg=bgColor, fg=textColor, font=("Helvetica", 11, "bold")).pack()
    # empty()
    updateTextChanges1 = Label(
        root, text="To see your changes in action,", bg=bgColor, fg=textColor, padx=5)
    updateTextChanges2 = Label(
        root, text="you must restart vMacro.", bg=bgColor, fg=textColor, padx=5)
    updateTextChanges1.pack()
    updateTextChanges2.pack()
    # empty(0.1)

    mainloop()


# openSettingsWindow()
