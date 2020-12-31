from tkinter import *
import os
from os import listdir
from os.path import isfile, join
import asyncio
import time


def changeProfFunc():
    pass


def createProfile():
    pass


def deleteProfiles():
    pass


def startMacroWindow():
    prof = Toplevel()
    prof.title("vMacro")
    profsTitle = Label(
        prof, text="Macros", pady="10", padx="5")
    profsTitle.pack()
    currentProfTxt = Label(
        prof, text="Current Profile: { }", pady="5", padx="5")
    currentProfTxt.pack()
    changeProfTxt = Button(
        prof, text="Change Profile", command=changeProfFunc)
    changeProfTxt.pack()
    createProfBtn = Button(
        prof, text="Create New Profile", command=createProfile)
    createProfBtn.pack()
    deleteProfsBtn = Button(
        prof, text="Delete All Profiles", command=deleteProfiles, padx="4")
    deleteProfsBtn.pack()
    mainloop()
