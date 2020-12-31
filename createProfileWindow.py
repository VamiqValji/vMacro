from tkinter import *
from tkinter import messagebox

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
    if len(profileName) > 0 and len(replaced) == 1 and len(replacement) == 1 and profileLoc != "Unset":
        profileLoc = (profileLoc.replace(" ", "")).lower()
        f = open(f"../vMacro/profiles/{profileLoc}/macro.txt", "w")
        # f = open("/profiles/" +{profileLoc.replace(" ", "")}/macro.txt", "w")
        f.write(f"{profileName}\n{replaced}\n{replacement}")
        f.close()
    else:
        popUp()


def createProfile():
    prof = Toplevel()
    createProfTitle = Label(
        prof, text="Profiles", pady="10", padx="5")
    createProfTitle.pack()
    # Input Field 1
    inpField1Txt = Label(
        prof, text="Profile Name", pady="5", padx="5")
    inpField1Txt.pack()
    inpField1Entry = Entry(
        prof, width="10")
    inpField1Entry.pack()
    # Input Field 2
    inpField2Txt = Label(
        prof, text="What key will be replaced?", pady="5", padx="5")
    inpField2Txt.pack()
    # inpField2Entry = Entry(
    #     prof, width="10")
    # inpField2Entry.pack()
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
    # Margin
    # spaceMargin = Label(
    #     prof, text="", pady="2", padx="0")
    # spaceMargin.pack()
    #
    # Submit
    submitBtn = Button(
        prof, text="Submit", pady="2", command=lambda: submitProfile(inpField1Entry.get(), dropDownReplaced.get(), dropDownReplacement.get(), dropWhichProfile.get()))
    submitBtn.pack()
    mainloop()
