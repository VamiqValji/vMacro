from tkinter import *
from tkinter import messagebox
from createProfileWindow import createProfile
from createProfileWindow import listOfLetters
import os
from os import listdir
from os.path import isfile, join
from defaultSettings import importDefaultSettings
from defaultSettings import getColor

listOfProfiles = ['Profile 1', 'Profile 2', 'Profile 3', 'Profile 4',
                  'Profile 5', 'Profile 6', 'Profile 7', 'Profile 8', 'Profile 9', 'Profile 10']
activeProfiles = ['Profile 1']


def openProfilesWindow():

    def addEmptySpace(amountOfEmptySpace):
        emptySpace = Label(
            prof, text="", pady=amountOfEmptySpace, padx="0", bg=bgColor, fg=textColor)
        emptySpace.pack()

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

    def profileSettingsFrame(profileNum):

        # profile name, profile replaced, profile replacement

        def submitChanges(profName, replaced, replacement):
            thisFolder = os.path.dirname(os.path.abspath(
                __file__)) + f"/profiles/profile{profileNum}/"
            my_file = os.path.join(thisFolder, "macro.txt")
            f = open(my_file, "w")
            f.write(f"{profName}\n{replaced}\n{replacement}")
            f.close()
            messagebox.showinfo("Settings Changed", "Submission complete.")

        # checkProfiles

        try:
            profileNum = int(str(profileNum)[-1:])

            # getData
            thisFolder = os.path.dirname(os.path.abspath(
                __file__)) + f"/profiles/profile{profileNum}/"
            my_file = os.path.join(thisFolder, "macro.txt")
            f = open(my_file, "r")
            profileInfo = f.readlines()
            f.close()
            pName = (profileInfo[0]).replace("\n", "")
            pReplaced = (profileInfo[1]).replace("\n", "")
            pReplacement = (profileInfo[2]).replace("\n", "")

            prof = Toplevel()
            bgColor = getColor("bg")
            textColor = getColor("text")
            importDefaultSettings(prof)
            prof.config(bg="black")
            # Input Field 1
            inpField1Txt = Label(
                prof, text=f"Edit Profile {str(profileNum)} ({pName})", pady="5", padx="5", bg=bgColor, fg=textColor)
            inpField1Txt.pack()
            # Input Field 2
            inpField2Txt = Label(
                prof, text="What key will be replaced?", pady="5", padx="5", bg=bgColor, fg=textColor)
            inpField2Txt.pack()
            dropDownReplaced = StringVar()
            dropDownReplaced.set(pReplaced)
            inpField2Drop = OptionMenu(
                prof, dropDownReplaced, *listOfLetters)
            inpField2Drop.pack()
            # Input Field 3
            inpField3Txt = Label(
                prof, text="What key would you like to map the replacement to?", pady="5", padx="5", bg=bgColor, fg=textColor)
            inpField3Txt.pack()
            dropDownReplacement = StringVar()
            dropDownReplacement.set(pReplacement)
            inpField3Drop = OptionMenu(
                prof, dropDownReplacement, *listOfLetters)
            inpField3Drop.pack()
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
            # Submit
            empty1 = Label(prof, text="", pady="2", bg=bgColor, fg=textColor)
            empty1.pack()
            submitBtn = Button(
                prof, text="Submit Changes", pady="0", padx="8", command=lambda: submitChanges(pName, dropDownReplaced.get(), dropDownReplacement.get()), bg=bgColor, fg=textColor)
            submitBtn.pack()
            empty2 = Label(prof, text="", pady="1", bg=bgColor, fg=textColor)
            empty2.pack()
        except:
            messagebox.showerror("Invalid Submission",
                                 "Please select a profile.")

    def deleteProfile(profName):
        profileNum = int(str(profName)[-1:])
        if profileNum == 1:
            messagebox.showerror("Invalid Deletion",
                                 "You can delete any profile except for Profile 1.")
        else:
            response = messagebox.askokcancel(
                "Delete Warning", f"You are about about to delete {profName}.")
            if response == 1:  # OK
                thisFolder = os.path.dirname(os.path.abspath(
                    __file__)) + f"/profiles/profile{profileNum}/"
                my_file = os.path.join(thisFolder, "macro.txt")
                os.remove(my_file)
            else:  # CANCEL
                pass

    checkProfiles()

    prof = Toplevel()
    bgColor = getColor("bg")
    textColor = getColor("text")
    importDefaultSettings(prof)
    profsTitle = Label(
        prof, text="Profile Settings", pady="10", padx="5", bg=bgColor, fg=textColor)
    profsTitle.pack()
    profInpTxt = Label(
        prof, text="Under which profile would you like to write / overwrite settings to?", pady="5", padx="5", bg=bgColor, fg=textColor)
    profInpTxt.pack()
    dropWhichProfile = StringVar()
    dropWhichProfile.set("Unset")
    print(activeProfiles)
    profInpDrop = OptionMenu(
        prof, dropWhichProfile, *activeProfiles)
    profInpDrop.pack()
    showSelectionTxt = Button(
        prof, text="Edit Selected Profile", pady="1", padx="5", command=lambda: profileSettingsFrame(dropWhichProfile.get()), bg=bgColor, fg=textColor)
    showSelectionTxt.pack()
    inpField4TxtSub = Label(
        prof, text="If your profile isn't showing, re-open this window.", pady="0", padx="0", bg=bgColor, fg=textColor)
    inpField4TxtSub.pack()
    addEmptySpace(.5)
    deleteProfsBtn = Button(
        prof, text="Delete Selected Profile", command=lambda: deleteProfile(dropWhichProfile.get()), padx="4", bg=bgColor, fg=textColor)
    deleteProfsBtn.pack()
    addEmptySpace(.5)
    createProfBtn = Button(
        prof, text="Create New Profile", command=createProfile, bg=bgColor, fg=textColor)
    createProfBtn.pack()
    addEmptySpace(.5)
    mainloop()


# openProfilesWindow()
