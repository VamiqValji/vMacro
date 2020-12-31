from tkinter import *
from tkinter import messagebox
from createProfileWindow import createProfile
from createProfileWindow import listOfLetters
from os import listdir
from os.path import isfile, join
# f = open("keysPressed_prev_log.txt", "r")
# prevLog = f.read()
# print(prevLog)


# def selectedProfile(profileNum):
#     print(profileNum)

listOfProfiles = ['Profile 1', 'Profile 2', 'Profile 3', 'Profile 4',
                  'Profile 5', 'Profile 6', 'Profile 7', 'Profile 8', 'Profile 9', 'Profile 10']
activeProfiles = ['Profile 1']


def openProfilesWindow():

    def addEmptySpace(amountOfEmptySpace):
        emptySpace = Label(
            prof, text="", pady=amountOfEmptySpace, padx="0")
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
        def submitChanges():
            print("changes submitted")
            pass

        # checkProfiles

        try:
            profileNum = int(str(profileNum)[-1:])

            def grabData():
                f = open(
                    f"..vMacro/profiles/profile{profileNum}/macro.txt", "r")
                print(f.read())
                f.close()
                pass

            prof = Toplevel()
            prof.title("vMacro")
            # Input Field 1
            inpField1Txt = Label(
                prof, text=f"Edit Profile {str(profileNum)}", pady="5", padx="5")
            inpField1Txt.pack()
            # Input Field 2
            inpField2Txt = Label(
                prof, text="What key will be replaced?", pady="5", padx="5")
            inpField2Txt.pack()
            dropDownReplaced = StringVar()
            dropDownReplaced.set("Unset")
            inpField2Drop = OptionMenu(
                prof, dropDownReplaced, *listOfLetters)
            inpField2Drop.pack()
            # Input Field 3
            inpField3Txt = Label(
                prof, text="What key would you like to map the replacement to?", pady="5", padx="5")
            inpField3Txt.pack()
            dropDownReplacement = StringVar()
            dropDownReplacement.set("Unset")
            inpField3Drop = OptionMenu(
                prof, dropDownReplacement, *listOfLetters)
            inpField3Drop.pack()
            # Example Description
            desc1Txt = Label(
                prof, text="Example: If 'w' was being replaced with 's',", pady="0", padx="8")
            desc1Txt.pack()
            desc2Txt = Label(
                prof, text="when 's' is pressed the 'w' key will be stimulated (as if it", pady="0", padx="8")
            desc2Txt.pack()
            desc3Txt = Label(
                prof, text="was being pressed by you) by the computer as well.", pady="0", padx="8")
            desc3Txt.pack()
            submitBtn = Button(
                prof, text="Submit Changes", pady="0", padx="8", command=submitChanges)
            submitBtn.pack()
        except:
            messagebox.showerror("Invalid Submission",
                                 "Please select a profile.")

    def deleteProfiles():
        pass

    checkProfiles()

    prof = Toplevel()
    prof.title("vMacro")
    profsTitle = Label(
        prof, text="Profile Settings", pady="10", padx="5")
    profsTitle.pack()
    profInpTxt = Label(
        prof, text="Under which profile would you like to write / overwrite settings to?", pady="5", padx="5")
    profInpTxt.pack()
    dropWhichProfile = StringVar()
    dropWhichProfile.set("Unset")
    print(activeProfiles)
    profInpDrop = OptionMenu(
        prof, dropWhichProfile, *activeProfiles)
    profInpDrop.pack()
    showSelectionTxt = Button(
        prof, text="Edit Selected Profile", pady="1", padx="5", command=lambda: profileSettingsFrame(dropWhichProfile.get()))
    showSelectionTxt.pack()
    inpField4TxtSub = Label(
        prof, text="If your profile isn't showing, refresh this window.", pady="0", padx="0")
    inpField4TxtSub.pack()
    addEmptySpace(.5)
    deleteProfsBtn = Button(
        prof, text="Delete Profiles", command=deleteProfiles, padx="4")
    deleteProfsBtn.pack()
    addEmptySpace(.5)
    createProfBtn = Button(
        prof, text="Create New Profile", command=createProfile)
    createProfBtn.pack()
    addEmptySpace(.5)
    mainloop()


openProfilesWindow()
