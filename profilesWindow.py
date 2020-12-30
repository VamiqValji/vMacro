from tkinter import *
from createProfileWindow import createProfile
# f = open("keysPressed_prev_log.txt", "r")
# prevLog = f.read()
# print(prevLog)


def openProfilesWindow():
    prof = Toplevel()
    prof.title("vMacro")
    profTitles = Label(
        prof, text="Profiles", pady="10", padx="5")
    profTitles.pack()
    createProfBtn = Button(
        prof, text="Create New Profile", command=createProfile)
    createProfBtn.pack()
    mainloop()
