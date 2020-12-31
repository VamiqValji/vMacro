from tkinter import *
from tkinter import messagebox
from createProfileWindow import createProfile
from createProfileWindow import listOfProfiles
from createProfileWindow import listOfLetters
# f = open("keysPressed_prev_log.txt", "r")
# prevLog = f.read()
# print(prevLog)


# def selectedProfile(profileNum):
#     print(profileNum)


def openProfilesWindow():

    def profileSettingsFrame(profileNum):

        try:
            profileNum = int(str(profileNum)[-1:])

            def grabData():
                # f = open(f"..vMacro/profiles/profile{profileNum}/macro.txt", "r")
                # f.read()
                # f.close()
                pass

            prof = Toplevel()
            prof.title("vMacro")
            # Input Field 1
            inpField1Txt = Label(
                prof, text=f"Edit Profile {str(profileNum)}", pady="5", padx="5")
            inpField1Txt.pack()
            # editProfTitle = Label(
            #     prof, text="Edit", pady="5", padx="5")
            # editProfTitle.pack()
            # inpField1Entry = Entry(
            #     prof, width="10")
            # inpField1Entry.pack()
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
            # Input Field 4
            inpField4Txt = Label(
                prof, text="Under which profile would you like to write / overwrite these settings to?", pady="5", padx="5")
            inpField4Txt.pack()
            dropWhichProfile = StringVar()
            dropWhichProfile.set("Unset")
            inpField4Drop = OptionMenu(
                prof, dropWhichProfile, *listOfProfiles)
            inpField4Drop.pack()
            # Example Description
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
        except:
            messagebox.showerror("Invalid Submission",
                                 "Please select a profile.")

    def addEmptySpace(amountOfEmptySpace):
        emptySpace = Label(
            prof, text="", pady=amountOfEmptySpace, padx="0")
        emptySpace.pack()

    prof = Toplevel()
    prof.title("vMacro")
    profsTitle = Label(
        prof, text="Profiles", pady="10", padx="5")
    profsTitle.pack()
    profInpTxt = Label(
        prof, text="Under which profile would you like to write / overwrite settings to?", pady="5", padx="5")
    profInpTxt.pack()
    dropWhichProfile = StringVar()
    dropWhichProfile.set("Unset")
    profInpDrop = OptionMenu(
        prof, dropWhichProfile, *listOfProfiles)
    profInpDrop.pack()
    showSelectionTxt = Button(
        prof, text="Edit Selected Profile", pady="5", padx="5", command=lambda: profileSettingsFrame(dropWhichProfile.get()))
    showSelectionTxt.pack()
    addEmptySpace(.5)
    addEmptySpace(.5)
    createProfBtn = Button(
        prof, text="Create New Profile", command=createProfile)
    createProfBtn.pack()
    addEmptySpace(.5)
    mainloop()


openProfilesWindow()
