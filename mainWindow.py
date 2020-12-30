from tkinter import *
import os
import asyncio
import time
from profilesWindow import openProfilesWindow
# from keys import runKeys

root = Tk()
root.title("vMacro")

# e = Entry(root, width=50)
# e.grid(row=3, column=0)

status = Label(root, text="Not Recording",  bd=1, relief=SUNKEN)


def onClick():
    # print("Clicked.")
    # print(e.get())
    global status
    try:
        if os.path.exists("keysRunning.txt") == False:
            os.startfile("keys.py")
            status['text'] = 'Recording'
        else:
            keysRunningLabel.grid(root, row=2, column=0, bd=5)
            # status['text'] = 'Not Recording'
        if os.path.exists("mouseRunning.txt") == False:
            os.startfile("mouse.py")
            status['text'] = 'Recording'
        else:
            mouseRunningLabel.grid(root, row=3, column=0)
            # status['text'] = 'Not Recording'
    except:
        pass


def resetScripts():
    if os.path.exists("keysRunning.txt"):
        os.remove("keysRunning.txt")
    if os.path.exists("mouseRunning.txt"):
        os.remove("mouseRunning.txt")


async def checkKeysRunning():
    while True:
        time.sleep(0.1)
        print("test")

# frame = LabelFrame(root, text="Click me!")
# Images
# myImg = ImageTk.PhotoImage(Image.open("/"))
runBtn = Button(root, text="Run", padx=10, pady=5, command=onClick)
resetBtn = Button(root, text="Reset", padx=10, pady=5, command=resetScripts)
profilesBtn = Button(root, text="Profiles",
                     padx=10, pady=5, bd=3, command=openProfilesWindow)

clickMeTxt = Label(root, text="Click me!")
resetTxt = Label(root, text="Not working? Click the reset button.")
mouseRunningLabel = Label(root, text="Mouse vMacro script is already running.")
keysRunningLabel = Label(
    root, text="Keyboard vMacro script is already running.")


runBtn.grid(row=1, column=0, padx=5, pady=5)
resetBtn.grid(row=4, column=0, padx=5, pady=5)
profilesBtn.grid(row=7, column=0, padx=10, pady=10)

resetTxt.grid(row=5, column=0, padx=5, pady=5)
status.grid(row=100, column=0, sticky=W+E)

# root.mainloop()

mainloop()
