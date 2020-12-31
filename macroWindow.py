from tkinter import *
import os
from os import listdir
from os.path import isfile, join
import asyncio
import time
from createProfileWindow import listOfProfiles
from profilesWindow import openProfilesWindow


activeProfiles = ['Profile 1']


def runMacro():
    pass

# def viewSelected():
#     pass


def startMacroWindow():

    def checkProfiles():
        global listOfProfiles
        global activeProfiles
        activeProfiles = []  # clean slate if any were deleted
        for i in range(1, 10):
            mypath = f"../vMacro/profiles/profile{i}"
            files = [f for f in listdir(mypath)]
            if "macro.txt" in files:
                print(f"Profile {i} has a macro file.")
                activeProfiles = activeProfiles + [f"Profile {i}"]

    def macroWindow():
        pass
    checkProfiles()
    prof = Toplevel()
    prof.title("vMacro")
    profsTitle = Label(
        prof, text="Macros", pady="10", padx="5")
    profsTitle.pack()
    dropVar = StringVar()
    dropVar.set("Unset")
    profDrop = OptionMenu(
        prof, dropVar, *activeProfiles)
    profDrop.pack()
    runBtn = Button(
        prof, text="Run", command=runMacro, padx="4")
    runBtn.pack()
    empty1 = Label(prof, text="", pady="2")
    empty1.pack()
    profSettingsBtn = Button(
        prof, text="Profiles Settings", command=openProfilesWindow, padx="4")
    profSettingsBtn.pack()
    mainloop()


# startMacroWindow()
