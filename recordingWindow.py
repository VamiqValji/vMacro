from tkinter import *
import os
from os import listdir
from os.path import isfile, join
import asyncio
import time
from profilesWindow import openProfilesWindow
from mouse import startMouseRecord
# from keys import startKBRecord
# from keys import replayKB
# from mouse import replayMouse

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
                # status['text'] = 'Recording'
                pass
            else:
                pass
            if os.path.exists("../vMacro/logs/mouseRunning.txt") == False:
                os.startfile('mouse.py')
                # status['text'] = 'Recording'
            else:
                pass
        except:
            pass

    def actualRecordingWindow(whatsBeingRecorded):

        whatsBeingRecorded = whatsBeingRecorded.replace("Record ", "")

        def RECORD(timeInterv, time, kbUnderstandInt):

            print(timeInterv)
            print(time)
            print(kbUnderstandInt)

            if whatsBeingRecorded == "Mouse":
                try:
                    if os.path.exists("../vMacro/logs/mouseRunning.txt") == False:
                        startMouseRecord(timeInterv, time)
                        # os.startfile('mouse.py')
                        # status['text'] = 'Recording'
                    else:
                        pass
                except:
                    pass
            elif whatsBeingRecorded == "Keyboard":
                try:
                    if kbUnderstandInt == 1:  # User understands how to stop keyboard recording
                        if os.path.exists("../vMacro/logs/keysRunning.txt") == False:
                            os.startfile("keys.py")
                            # startKBRecord()
                            # status['text'] = 'Recording'
                            pass
                        else:
                            pass
                    else:
                        pass
                except:
                    pass
            else:  # KB & M
                pass

        def REPLAY(timeInterv, time):
            if whatsBeingRecorded == "Mouse":
                pass
            elif whatsBeingRecorded == "Keyboard":
                pass
            else:  # KB & M
                pass

        root = Tk()
        root.title("vMacro")

        title = Label(
            root, text=f"Record: {whatsBeingRecorded}", pady="10", padx="5")
        title.pack()

        eTimeInterval = Entry(root)
        eTime = Entry(root)

        def renderMouseSettings():
            global eTimeInterval
            global eTime
            mouseSettingsTitle = Label(
                root, text="Mouse Settings", pady="12", padx="5")
            mouseSettingsTitle.pack()
            instructionsTxtMouse = Label(
                root, text="To end the mouse recording once its started, move your mouse.", pady="8", padx="5")
            intervalTxt1 = Label(
                root, text="Enter a time interval for mouse tracking;", pady="0", padx="5")
            intervalTxt2 = Label(
                root, text="the lower the number, the smoother the tracking.", pady="0", padx="5")
            eTimeInterval = Entry(root)
            eTimeInterval.insert(0, '0.1')
            intervalTxt3 = Label(
                root, text="Enter the amount of time the mouse will be tracked", pady="8", padx="5")
            eTime = Entry(root)
            eTime.insert(0, 'username')
            instructionsTxtMouse.pack()
            intervalTxt1.pack()
            intervalTxt2.pack()
            eTimeInterval.pack()
            intervalTxt3.pack()
            eTime.pack()

        understandVar = IntVar()
        understandVar.set(0)

        def renderKBSettings():
            global understandVar
            KBSettingsTitle = Label(
                root, text="Keyboard Settings", pady="12", padx="5")
            instructionsTxtKB1 = Label(
                root, text="To end the keyboard recording", pady="4", padx="5")
            instructionsTxtKB2 = Label(
                root, text="once its started, hit escape.", pady="0", padx="5")
            # iUnderstandDropDown = StringVar()
            # iUnderstandDropDown.set("Unset")
            # inpFieldDrop = OptionMenu(
            #     root, iUnderstandDropDown, *["I Understand."])
            understandVar = IntVar()
            understandVar.set(0)
            iUnderstand1 = Radiobutton(root, text="I Do Not Understand.",
                                       variable=understandVar, value=0)
            iUnderstand2 = Radiobutton(root, text="I Understand.",
                                       variable=understandVar, value=1)
            KBSettingsTitle.pack()
            instructionsTxtKB1.pack()
            instructionsTxtKB2.pack()
            iUnderstand1.pack()
            iUnderstand2.pack()
            # inpFieldDrop.pack()

        if whatsBeingRecorded == "Mouse":
            renderMouseSettings()
        elif whatsBeingRecorded == "Keyboard":
            renderKBSettings()
        else:  # KB & M
            renderMouseSettings()
            renderKBSettings()

        empty3 = Label(root, text="", pady=6)
        empty3.pack()
        recordBtn = Button(root, text="Start Recording",
                           padx=10, pady=10, command=lambda: RECORD(eTimeInterval.get(), eTime.get(), understandVar.get()))
        resetBtn = Button(root, text="Reset", padx=10,
                          pady=5, command=resetScripts)

        resetTxt = Label(root, text="Not working? Click the reset button.")

        empty4 = Label(root, text="", pady=8)
        replayBtn = Button(root, text="REPLAY", padx=10,
                           pady=10, command=REPLAY(eTimeInterval.get(), eTime.get()))
        empty5 = Label(root, text="", pady=5)

        recordBtn.pack()
        resetBtn.pack()
        resetTxt.pack()

        empty4.pack()
        replayBtn.pack()
        empty5.pack()

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
