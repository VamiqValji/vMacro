from tkinter import *
import os
from os import listdir
from os.path import isfile, join
import asyncio
import time
from profilesWindow import openProfilesWindow

# from keys import runKeys


def startRecordingWindow():

    def resetScripts():
        try:
            if os.path.exists("../vMacro/logs/keysRunning.txt"):
                os.remove("../vMacro/logs/keysRunning.txt")
            if os.path.exists("../vMacro/logs/mouseRunning.txt"):
                os.remove("../vMacro/logs/mouseRunning.txt")
        except:
            pass

    def record():
        try:
            if os.path.exists("../vMacro/logs/keysRunning.txt") == False:
                os.startfile("keys.py")
                status['text'] = 'Recording'
            else:
                keysRunningLabel.grid(root, row=6, column=0)
            if os.path.exists("../vMacro/logs/mouseRunning.txt") == False:
                os.startfile('mouse.py')
                status['text'] = 'Recording'
            else:
                mouseRunningLabel.grid(root, row=7, column=0)
        except:
            pass

    def actualRecordingWindow(whatsBeingRecorded):
        root = Tk()
        root.title("vMacro")

        whatsBeingRecorded = whatsBeingRecorded.replace("Record ", "")

        title = Label(
            root, text=f"Record: {whatsBeingRecorded}", pady="10", padx="5")
        title.pack()

        recordBtn = Button(root, text="Start Recording",
                           padx=10, pady=5, command=record)
        resetBtn = Button(root, text="Reset", padx=10,
                          pady=5, command=resetScripts)

        resetTxt = Label(root, text="Not working? Click the reset button.")
        empty = Label(
            root, text="")

        recordBtn.pack()
        empty.pack()
        resetBtn.pack()
        resetTxt.pack()

        def renderMouseSettings():
            mouseSettingsTitle = Label(
                root, text="Mouse Settings", pady="12", padx="5")

        def renderKBSettings():
            KBSettingsTitle = Label(
                root, text="Keyboard Settings", pady="12", padx="5")

        if whatsBeingRecorded == "Mouse":
            renderMouseSettings()
        elif whatsBeingRecorded == "Keyboard":
            renderKBSettings()
        else:  # KB & M
            renderMouseSettings()
            renderKBSettings()

        mainloop()

    root = Tk()
    root.title("vMacro")

    title = Label(
        root, text="Recordings", pady="10", padx="5")
    title.grid(row=0, column=0)
    instructions = Label(
        root, text="Choose What To Record:", pady="4", padx="5")

    # status = Label(root, text="Not Recording",  bd=1, relief=SUNKEN)

    dropDown = StringVar()
    dropDown.set("Unset")
    inpFieldDrop = OptionMenu(
        root, dropDown, *["Record Mouse", "Record Keyboard", "Record Mouse & KB"])
    openRecordingBtn = Button(
        root, text="Open Recording Window", padx=10, pady=5, command=lambda: actualRecordingWindow(dropDown.get()))

    # resetTxt = Label(root, text="Not working? Click the reset button.")
    # mouseRunningLabel = Label(
    #     root, text="Mouse vMacro script is already running.")
    # keysRunningLabel = Label(
    #     root, text="Keyboard vMacro script is already running.")
    empty = Label(
        root, text="")

    instructions.grid(row=1, column=0, padx=5, pady=5)
    inpFieldDrop.grid(row=2, column=0, padx=5, pady=5)
    openRecordingBtn.grid(row=3, column=0, padx=5, pady=5)
    empty.grid(row=4, column=0, padx=5, pady=1)
    # resetBtn.grid(row=5, column=0, padx=5, pady=1)

    # resetTxt.grid(row=6, column=0, padx=5, pady=5)
    # status.grid(row=100, column=0, sticky=W+E)

    # root.mainloop()

    mainloop()


startRecordingWindow()
