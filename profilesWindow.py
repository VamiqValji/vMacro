from tkinter import *
from tkinter import messagebox
from createProfileWindow import createProfile
from createProfileWindow import listOfLetters
import os
from os import listdir
from os.path import isfile, join
from os import path
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
                # print(f"Profile {i} has a macro file.")
                activeProfiles = activeProfiles + [f"Profile {i}"]

    def profileSettingsFrame(profileNum):

        global dropDownReplaced
        global drownDownReplacement

        # profile name, profile replaced, profile replacement

        def submitChanges(profName, replaced, replacement, profileLoc):
            # thisFolder = os.path.dirname(os.path.abspath(
            #     __file__)) + f"/profiles/profile{profileNum}/"
            # my_file = os.path.join(thisFolder, "macro.txt")
            # f = open(my_file, "w")
            # f.write(f"{profName}\n{replaced}\n{replacement}")
            # f.close()
            # messagebox.showinfo("Settings Changed", "Submission complete.")

            profileLoc = (profileLoc.replace(" ", "")).lower()
            profFolder = os.path.dirname(os.path.abspath(
                __file__)) + f"/profiles/{profileLoc}/"  # + f"/logs/"

            if len(profName) > 0 and replaced != "Unset" and replacement != "Unset" and profileLoc != "Unset":
                profileLoc = (profileLoc.replace(" ", "")).lower()

                if path.exists(os.path.join(profFolder, "recordingReplaced.txt")):
                    f = open(os.path.join(profFolder, "recordingReplaced.txt"))
                    replaced = f.readlines()[0]
                    f.close()
                    os.remove(os.path.join(
                        profFolder, "recordingReplaced.txt"))

                if path.exists(os.path.join(profFolder, "recordingReplacement.txt")):
                    f = open(os.path.join(
                        profFolder, "recordingReplacement.txt"))
                    replacement = f.readlines()[0]
                    f.close()
                    os.remove(os.path.join(
                        profFolder, "recordingReplacement.txt"))

                f = open(f"../vMacro/profiles/{profileLoc}/macro.txt", "w")
                f.write(f"{profName}\n{replaced}\n{replacement}")
                f.close()
                messagebox.showinfo("Profile Success",
                                    "Profile addition / changes have been made.")
            else:
                messagebox.showerror("Invalid Submission",
                                     "Please fill out all of the inputs of the form.")

        def recordHandler(replaced, replacement, profileLoc, recordedReplaced=False, recordedReplacement=False):

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
                f.close()

                os.startfile("recordKeyInput.py")
                if recordedReplaced == True:
                    dropDownReplaced.set("Recorded / Recording")
                if recordedReplacement == True:
                    dropDownReplacement.set("Recorded / Recording")
            except:
                messagebox.showerror("Error", "Please select a profile first.")

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

            # Input Field 1
            inpField1Txt = Label(
                prof, text=f"Edit Profile {str(profileNum)} ({pName})", pady="5", padx="5", bg=bgColor, fg=textColor, font=("Helvetica", 18, "bold"))
            inpField1Txt.pack()
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
            # Input Field 2
            inpField2Txt = Label(
                prof, text="What key will be replaced?", pady="5", padx="5", bg=bgColor, fg=textColor, font=("Helvetica", 11))
            inpField2Txt.pack()
            dropDownReplaced = StringVar()
            dropDownReplaced.set(str(pReplaced).replace("Key.", ""))
            inpField2Drop = OptionMenu(
                prof, dropDownReplaced, *listOfLetters)
            inpField2Drop.pack()
            Button(prof, text="Record Replaced Key", pady=0,
                   padx=2, command=lambda: recordHandler(dropDownReplaced.get(), dropDownReplacement.get(), dropWhichProfile.get(), True, False), bg=bgColor, fg=textColor, font=("Helvetica", 11, "bold")).pack()
            # Input Field 3
            inpField3Txt = Label(
                prof, text="What key would you like to map the replacement to?", pady="5", padx="5", bg=bgColor, fg=textColor, font=("Helvetica", 11))
            inpField3Txt.pack()
            dropDownReplacement = StringVar()
            dropDownReplacement.set(str(pReplacement).replace("Key.", ""))
            inpField3Drop = OptionMenu(
                prof, dropDownReplacement, *listOfLetters)
            inpField3Drop.pack()
            #
            Button(prof, text="Record Replacement Key", pady=0,
                   padx=2, command=lambda: recordHandler(dropDownReplaced.get(), dropDownReplacement.get(), dropWhichProfile.get(), False, True), bg=bgColor, fg=textColor, font=("Helvetica", 11, "bold")).pack()
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
            # Submit
            empty1 = Label(prof, text="", pady="2", bg=bgColor, fg=textColor)
            empty1.pack()

            def beforeSubmitChanges(profileName, replaced, replacement, profileLoc):
                dropDownReplaced.set("Unset")
                dropDownReplacement.set("Unset")
                submitChanges(profileName, replaced, replacement, profileLoc)

            submitBtn = Button(
                prof, text="Submit Changes", pady="0", padx="8", command=lambda: beforeSubmitChanges(pName, dropDownReplaced.get(), dropDownReplacement.get(), dropWhichProfile.get()), bg=bgColor, fg=textColor, font=("Helvetica", 11, "bold"))
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
        prof, text="Profile Settings", pady="10", padx="5", bg=bgColor, fg=textColor, font=("Helvetica", 18, "bold"))
    profsTitle.pack()
    profInpTxt = Label(
        prof, text="Under which profile would you like to write / overwrite settings to?", pady="5", padx="5", bg=bgColor, fg=textColor, font=("Helvetica", 11))
    profInpTxt.pack()
    dropWhichProfile = StringVar()
    dropWhichProfile.set("Unset")
    profInpDrop = OptionMenu(
        prof, dropWhichProfile, *activeProfiles)
    profInpDrop.pack()
    showSelectionTxt = Button(
        prof, text="Edit Selected Profile", pady="1", padx="5", command=lambda: profileSettingsFrame(dropWhichProfile.get()), bg=bgColor, fg=textColor, font=("Helvetica", 11, "bold"))
    showSelectionTxt.pack()
    inpField4TxtSub = Label(
        prof, text="If your profile isn't showing, re-open this window.", pady="0", padx="0", bg=bgColor, fg=textColor)
    inpField4TxtSub.pack()
    addEmptySpace(.5)
    deleteProfsBtn = Button(
        prof, text="Delete Selected Profile", command=lambda: deleteProfile(dropWhichProfile.get()), padx="4", bg=bgColor, fg=textColor, font=("Helvetica", 11, "bold"))
    deleteProfsBtn.pack()
    addEmptySpace(.5)
    createProfBtn = Button(
        prof, text="Create New Profile", command=createProfile, bg=bgColor, fg=textColor, font=("Helvetica", 11, "bold"))
    createProfBtn.pack()
    addEmptySpace(.5)
    mainloop()


# openProfilesWindow()
