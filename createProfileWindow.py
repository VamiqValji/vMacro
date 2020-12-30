from tkinter import *

# f = open("keysPressed_prev_log.txt", "r")
# prevLog = f.read()
# print(prevLog)


def createProfile():
    prof = Toplevel()
    createProfBtn = Button(
        prof, text="Create New Profile", command=createProfile)
    createProfBtn.pack()
    mainloop()
