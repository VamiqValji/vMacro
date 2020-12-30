from tkinter import *

# f = open("keysPressed_prev_log.txt", "r")
# prevLog = f.read()
# print(prevLog)


def submitProfile(profileName):
    print(profileName)


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
    inpField2Entry = Entry(
        prof, width="10")
    inpField2Entry.pack()
    # Input Field 3
    inpField3Txt = Label(
        prof, text="What key would you like to map the replacement to?", pady="5", padx="5")
    inpField3Txt.pack()
    inpField3Entry = Entry(
        prof, width="10")
    inpField3Entry.pack()
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
        prof, text="Submit", pady="2", command=lambda: submitProfile(inpField1Entry.get()))
    submitBtn.pack()
    mainloop()
