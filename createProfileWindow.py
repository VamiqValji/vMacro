from tkinter import *
from tkinter import messagebox
from defaultSettings import importDefaultSettings
from defaultSettings import getColor
import os
from os import path
from os import listdir
from os.path import isfile, join
# from recordKeyInput import getInfo
import time

# f = open("keysPressed_prev_log.txt", "r")
# prevLog = f.read()
# print(prevLog)

listOfLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

listOfProfiles = ['Profile 1', 'Profile 2', 'Profile 3', 'Profile 4',
                  'Profile 5', 'Profile 6', 'Profile 7', 'Profile 8', 'Profile 9', 'Profile 10']


def popUp():
    # showwarning
    messagebox.showerror("Invalid Submission",
                         "Please fill out all of the inputs of the form.")


def submitProfile(profileName, replaced, replacement, profileLoc):

    print(profileName)
    print(replaced)
    print(replacement)
    print(profileLoc)
    if len(profileName) > 0 and replaced != "Unset" and replacement != "Unset" and profileLoc != "Unset":
        profileLoc = (profileLoc.replace(" ", "")).lower()

        if path.exists(os.path.join(profFolder, "recordingReplaced.txt")):
            f = open(os.path.join(profFolder, "recordingReplaced.txt"))
            replaced = f.readlines()[0]
            f.close()
            os.remove(os.path.join(profFolder, "recordingReplaced.txt"))

        if path.exists(os.path.join(profFolder, "recordingReplacement.txt")):
            f = open(os.path.join(profFolder, "recordingReplacement.txt"))
            replacement = f.readlines()[0]
            f.close()
            os.remove(os.path.join(profFolder, "recordingReplacement.txt"))

        f = open(f"../vMacro/profiles/{profileLoc}/macro.txt", "w")
        f.write(f"{profileName}\n{replaced}\n{replacement}")
        f.close()
        messagebox.showinfo("Profile Success",
                            "Profile addition / changes have been made.")
    else:
        popUp()


def createProfile():

    global dropDownReplaced
    global drownDownReplacement

    def recordHandler(profileName, replaced, replacement, profileLoc, recordedReplaced=False, recordedReplacement=False):

        global profFolder
        profileLoc = (profileLoc.replace(" ", "")).lower()
        profFolder = os.path.dirname(os.path.abspath(
            __file__)) + f"/profiles/{profileLoc}/"  # + f"/logs/"

        try:
            f = open(
                f"../vMacro/profiles/{profileLoc}/recordingInputInfo.txt", "w")
            if recordedReplaced == True:
                f.write(f"replaced")
            elif recordedReplacement == True:
                f.write(f"replacement")
            f.close()

            f = open(
                f"../vMacro/profiles/profNum.txt", "w")
            f.write(profileLoc)
            # print(profileLoc)
            f.close()

            os.startfile("recordKeyInput.py")
            if recordedReplaced == True:
                dropDownReplaced.set("Recorded / Recording")
            if recordedReplacement == True:
                dropDownReplacement.set("Recorded / Recording")
        except:
            messagebox.showerror("Error", "Please select a profile first.")

    prof = Toplevel()
    bgColor = getColor("bg")
    textColor = getColor("text")
    importDefaultSettings(prof)
    createProfTitle = Label(
        prof, text="Create Profile", pady="10", padx="5", bg=bgColor, fg=textColor, font=("Helvetica", 18, "bold"))
    createProfTitle.pack()
    # Input Field 1
    inpField1Txt = Label(
        prof, text="Profile Name", pady="5", padx="5", bg=bgColor, fg=textColor, font=("Helvetica", 11))
    inpField1Txt.pack()
    inpField1Txt.pack()
    inpField1Entry = Entry(
        prof, width="10", bg=bgColor, fg=textColor)
    inpField1Entry.pack()
    # Description / Instructions
    Label(
        prof, text="", pady="1", padx="5", bg=bgColor, fg=textColor).pack()
    Label(
        prof, text="Instead of using the option menu to select your key,", pady="0", padx="0", bg=bgColor, fg=textColor, font=("Helvetica", 10)).pack()
    Label(
        prof, text="you can select a key by pressing that key on your", pady="5", padx="0", bg=bgColor, fg=textColor, font=("Helvetica", 10)).pack()
    Label(
        prof, text="keyboard after pressing the corresponding record buttons.", pady="0", padx="5", bg=bgColor, fg=textColor, font=("Helvetica", 10)).pack()
    Label(
        prof, text="", pady="1", padx="5", bg=bgColor, fg=textColor).pack()
    # Input Field 4
    inpField4Txt = Label(
        prof, text="Under which profile would you like to write / overwrite these settings to?", pady="5", padx="5", bg=bgColor, fg=textColor, font=("Helvetica", 11))
    inpField4Txt.pack()
    dropWhichProfile = StringVar()
    dropWhichProfile.set("Unset")
    inpField4Drop = OptionMenu(
        prof, dropWhichProfile, *listOfProfiles)
    inpField4Drop.pack()
    # Input Field 2
    inpField2Txt = Label(
        prof, text="What key will be replaced?", pady="5", padx="5", bg=bgColor, fg=textColor, font=("Helvetica", 11))
    inpField2Txt.pack()
    dropDownReplaced = StringVar()
    dropDownReplaced.set("Unset")
    inpField2Drop = OptionMenu(
        prof, dropDownReplaced, *listOfLetters)
    inpField2Drop.pack()
    #
    Button(prof, text="Record Replaced Key", pady=0,
           padx=2, command=lambda: recordHandler(inpField1Entry.get(), dropDownReplaced.get(), dropDownReplacement.get(), dropWhichProfile.get(), True, False), bg=bgColor, fg=textColor, font=("Helvetica", 11, "bold")).pack()
    #
    # Input Field 3
    inpField3Txt = Label(
        prof, text="What key would you like to map the replacement to?", pady="5", padx="5", bg=bgColor, fg=textColor, font=("Helvetica", 11))
    inpField3Txt.pack()
    dropDownReplacement = StringVar()
    dropDownReplacement.set("Unset")
    inpField3Drop = OptionMenu(
        prof, dropDownReplacement, *listOfLetters)
    inpField3Drop.pack()
    #
    Button(prof, text="Record Replacement Key", pady=0,
           padx=2, command=lambda: recordHandler(inpField1Entry.get(), dropDownReplaced.get(), dropDownReplacement.get(), dropWhichProfile.get(), False, True), bg=bgColor, fg=textColor, font=("Helvetica", 11, "bold")).pack()
    #

    # Example Description
    desc1Txt = Label(
        prof, text="Example: If 'w' was being replaced with 's',", pady="0", padx="8", bg=bgColor, fg=textColor)
    desc1Txt.pack()
    desc2Txt = Label(
        prof, text="when 's' is pressed the 'w' key will be stimulated (as if it", pady="0", padx="8", bg=bgColor, fg=textColor)
    desc2Txt.pack()
    desc3Txt = Label(
        prof, text="was being pressed by you) by the computer as well.", pady="0", padx="8", bg=bgColor, fg=textColor)
    desc3Txt.pack()

    def beforeSubmitProfile(profileName, replaced, replacement, profileLoc):
        dropDownReplaced.set("Unset")
        dropDownReplacement.set("Unset")
        submitProfile(profileName, replaced, replacement, profileLoc)

    Label(
        prof, text="", pady="1", padx="5", bg=bgColor, fg=textColor).pack()
    submitBtn = Button(
        prof, text="Submit", pady="2", command=lambda: beforeSubmitProfile(inpField1Entry.get(), dropDownReplaced.get(), dropDownReplacement.get(), dropWhichProfile.get()), bg=bgColor, fg=textColor, font=("Helvetica", 11, "bold"))
    submitBtn.pack()
    Label(
        prof, text="", pady="1", padx="5", bg=bgColor, fg=textColor).pack()
    mainloop()


# createProfile()
