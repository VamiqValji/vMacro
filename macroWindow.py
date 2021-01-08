from tkinter import *
from tkinter import messagebox
import os
from os import listdir
from os.path import isfile, join
import asyncio
import time
from createProfileWindow import listOfProfiles
from profilesWindow import openProfilesWindow
from runKeysMacro import runKeysMacro
from defaultSettings import importDefaultSettings
from defaultSettings import getColor

activeProfiles = ['Profile 1']


def startMacroWindow():

    def checkProfiles():
        global listOfProfiles
        global activeProfiles
        activeProfiles = []  # clean slate if any were deleted
        for i in range(1, 10):
            mypath = f"../vMacro/profiles/profile{i}"
            files = [f for f in listdir(mypath)]
            if "macro.txt" in files:
                # print(f"Profile {i} has a macro file.")
                activeProfiles = activeProfiles + [f"Profile {i}"]

    def viewProfile(profileNum):
        try:
            profileNum = int(str(profileNum)[-1:])
            # getData
            runTxt["text"] = "Hit escape to exit the macro!"
            thisFolder = os.path.dirname(os.path.abspath(
                __file__)) + f"/profiles/profile{profileNum}/"
            my_file = os.path.join(thisFolder, "macro.txt")
            f = open(my_file, "r")
            profileInfo = f.readlines()
            f.close()
            pName = (profileInfo[0]).replace("\n", "")
            pReplaced = (profileInfo[1]).replace("\n", "")
            pReplacement = (profileInfo[2]).replace("\n", "")
            profSettingsTxt1["text"] = f"For Profile {profileNum} ({pName}):"
            pReplaced = str(pReplaced).replace("Key.", "")
            pReplacement = str(pReplacement).replace("Key.", "")
            profSettingsTxt2["text"] = f"'{pReplaced}' will be mapped to '{pReplacement}'."
        except:
            messagebox.showerror(
                "Invalid Profile", "Please select a valid profile.")

    def runKeyMacro(profileNum):
        try:
            runKeysMacro(profileNum)  # External python script
        except:
            messagebox.showerror(
                "Invalid Profile", "Please select a valid profile.")

    checkProfiles()
    prof = Toplevel()
    bgColor = getColor("bg")
    textColor = getColor("text")
    importDefaultSettings(prof)
    profsTitle = Label(
        prof, text="Macros", pady="10", padx="5", bg=bgColor, fg=textColor, font=("Helvetica", 18, "bold"))
    profsTitle.pack()
    dropVar = StringVar()
    dropVar.set("Unset")
    profDrop = OptionMenu(
        prof, dropVar, *activeProfiles)
    profDrop.pack()
    runBtn = Button(
        prof, text="Run", command=lambda: runKeyMacro(dropVar.get()), padx="4", bg=bgColor, fg=textColor, font=("Helvetica", 11, "bold"))
    runBtn.pack()
    empty2 = Label(prof, text="", pady="2", bg=bgColor, fg=textColor)
    empty2.pack()
    profSettingsBtn = Button(
        prof, text="View Selected Profile's Settings", command=lambda: viewProfile(dropVar.get()), padx="4", bg=bgColor, fg=textColor, font=("Helvetica", 11, "bold"))
    profSettingsBtn.pack()
    runTxt = Label(
        prof, text="", padx="4", bg=bgColor, fg=textColor)
    runTxt.pack()
    empty1 = Label(prof, text="", pady="2", bg=bgColor, fg=textColor)
    empty1.pack()
    profSettingsTxt1 = Label(
        prof, text=f"For Unset Profile:", pady="2", bg=bgColor, fg=textColor, font=("Helvetica", 11))
    profSettingsTxt1.pack()
    profSettingsTxt2 = Label(
        prof, text=f"Please Select A Profile", pady="2", bg=bgColor, fg=textColor, font=("Helvetica", 11))
    profSettingsTxt2.pack()
    empty3 = Label(prof, text="", pady="1", bg=bgColor, fg=textColor)
    empty3.pack()
    profSettingsBtn = Button(
        prof, text="Profiles Settings", command=openProfilesWindow, padx="4", bg=bgColor, fg=textColor, font=("Helvetica", 11, "bold"))
    profSettingsBtn.pack()
    empty4 = Label(prof, text="", pady="1", bg=bgColor, fg=textColor)
    empty4.pack()
    mainloop()


# startMacroWindow()
