from tkinter import *
from tkinter import messagebox
import os
from os import listdir
from os.path import isfile, join
import asyncio
import time
from profilesWindow import openProfilesWindow
# from replayWindow import REPLAY
# from mouse import startMouseRecord
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

    # def record():
    #     try:
    #         if os.path.exists("../vMacro/logs/keysRunning.txt") == False:
    #             os.startfile("keys.py")
    #             # status['text'] = 'Recording'
    #             pass
    #         else:
    #             pass
    #         if os.path.exists("../vMacro/logs/mouseRunning.txt") == False:
    #             os.startfile('mouse.py')
    #             # status['text'] = 'Recording'
    #         else:
    #             pass
    #     except:
    #         pass

    def actualRecordingWindow(whatsBeingRecorded):

        whatsBeingRecorded = whatsBeingRecorded.replace("Record ", "")

        def RECORD(timeInterv, time, kbUnderstand):

            def startMouseRecord(timeInter, time):

                # f = open("logs/replaySettings.txt", "w")
                # f.write(
                #     f"{timeInterv}\n{time}")
                # f.close()
                # os.startfile("replay.py")

                f = open("../vMacro/logs/mouseRunSettings.txt", "w")
                f.write(f"{timeInter}\n{time}")
                f.close()
                os.startfile("mouse.py")

            print(timeInterv)
            print(time)
            print(kbUnderstand)

            if "Unset" in whatsBeingRecorded:
                messagebox.showerror(
                    "Invalid Submission", "Please fill in all the required information correctly.")
            elif whatsBeingRecorded == "Mouse":
                try:
                    if timeInterv.replace(".", "").isdigit() and time.replace(".", "").isdigit():
                        try:
                            timeInterv = int(timeInterv)
                            time = int(time)
                        except:
                            timeInterv = float(timeInterv)
                            time = float(time)

                        if timeInterv >= 0.05:
                            if os.path.exists("../vMacro/logs/mouseRunning.txt") == False:
                                startMouseRecord(timeInterv, time)
                                # os.startfile('mouse.py')
                                # status['text'] = 'Recording'
                        else:
                            return messagebox.showerror(
                                "Incorrect Submission.", "Please make sure the inputted time interval is equal to or atleast 0.05.")
                    else:
                        messagebox.showerror(
                            "Incorrect Submission.", "Please select valid inputs (numbers).")
                except:
                    pass
            elif whatsBeingRecorded == "Keyboard":
                try:
                    if kbUnderstand != "Unset":  # User understands how to stop keyboard recording
                        if os.path.exists("../vMacro/logs/keysRunning.txt") == False:
                            os.startfile("keys.py")
                            # startKBRecord()
                            # status['text'] = 'Recording'
                            pass
                        else:
                            pass
                    else:
                        messagebox.showerror(
                            "Incorrect Submission.", "Please fill in all forms correctly.")
                except:
                    pass
            else:  # KB & M
                if kbUnderstand != "Unset" and timeInterv.replace(".", "").isdigit() and time.replace(".", "").isdigit():
                    if os.path.exists("../vMacro/logs/mouseRunning.txt") == False:
                        startMouseRecord(timeInterv, time)
                    if os.path.exists("../vMacro/logs/keysRunning.txt") == False:
                        os.startfile("keys.py")
                else:
                    messagebox.showerror(
                        "Incorrect Submission.", "Please fill in all forms correctly.")

        root = Tk()
        root.title("vMacro")

        title = Label(
            root, text=f"Record: {whatsBeingRecorded}", pady="10", padx="5")
        title.pack()

        global eTimeInterval
        global eTime
        eTimeInterval = Entry(root)
        eTime = Entry(root)
        eTimeInterval.insert(0, '0.1')
        eTime.insert(0, '1')

        def renderRecordBtn():
            Button(root, text="Start Recording",
                   padx=10, pady=10, command=lambda: RECORD(eTimeInterval.get(), eTime.get(), iUnderstandDropDown.get())).pack()

        def renderMouseSettings():

            mouseSettingsTitle = Label(
                root, text="Mouse Settings", pady="12", padx="5")
            mouseSettingsTitle.pack()
            instructionsTxtMouse = Label(
                root, text="To end the mouse recording once its started, move your mouse.", pady="8", padx="5")
            intervalTxt1 = Label(
                root, text="Enter a time interval for mouse tracking (seconds);", pady="0", padx="5")
            intervalTxt2 = Label(
                root, text="the lower the number, the smoother the tracking.", pady="0", padx="5")
            intervalTxt3 = Label(
                root, text="Enter the amount of time the mouse will be tracked (seconds)", pady="8", padx="5")
            instructionsTxtMouse.pack()
            intervalTxt1.pack()
            intervalTxt2.pack()
            eTimeInterval.pack()
            intervalTxt3.pack()
            eTime.pack()
            if whatsBeingRecorded == "Mouse":
                renderRecordBtn()

        global iUnderstandDropDown
        iUnderstandDropDown = StringVar()
        iUnderstandDropDown.set("Unset")

        def renderKBSettings():
            KBSettingsTitle = Label(
                root, text="Keyboard Settings", pady="12", padx="5")
            instructionsTxtKB1 = Label(
                root, text="To end the keyboard recording", pady="4", padx="5")
            instructionsTxtKB2 = Label(
                root, text="once its started, hit escape.", pady="0", padx="5")

            inpFieldDrop = OptionMenu(
                root, iUnderstandDropDown, *["I Understand."])
            # understandVar = IntVar()
            # understandVar.set(0)
            # iUnderstand1 = Radiobutton(root, text="I Do Not Understand.",
            #                            variable=understandVar, value=0)
            # iUnderstand2 = Radiobutton(root, text="I Understand.",
            #                            variable=understandVar, value=1)
            KBSettingsTitle.pack()
            instructionsTxtKB1.pack()
            instructionsTxtKB2.pack()
            # iUnderstand1.pack()
            # iUnderstand2.pack()
            inpFieldDrop.pack()
            renderRecordBtn()

        if "Unset" in whatsBeingRecorded:
            messagebox.showerror("Invalid Submission",
                                 "Please choose what you would like to record.")
        elif whatsBeingRecorded == "Mouse":
            renderMouseSettings()
        elif whatsBeingRecorded == "Keyboard":
            renderKBSettings()
        else:  # KB & M
            renderMouseSettings()
            renderKBSettings()

        def REPLAY(timeInterv, time, whatsBeingRecorded, kbUnderstand, loopAmount, runSpeed):

            if loopAmount.replace(".", "").isdigit() and runSpeed.replace(".", "").isdigit():
                f = open("../vMacro/logs/replaySettings.txt", "w")
                f.write(f"{loopAmount}\n{runSpeed}")
                f.close()
            else:
                return messagebox.showerror(
                    "Invalid Submission", "Please fill in all the required information correctly.")

            def checkMouse():
                fM = open("..vMacro/logs/mouseMonitor.txt", "r")
                read = fM.read()
                fM.close()
                if read == "":
                    return messagebox.showerror(
                        "Replay Error", "You can not replay anything until you record something first.")

            def checkKB():
                fK = open("logs/keysPressed.txt", "r")
                read = fK.read()
                fK.close()
                if read == "":
                    return messagebox.showerror(
                        "Replay Error", "You can not replay anything until you record something first.")

            # timeInterv, time, whatsBeingRecorded, kbUnderstand
            def startReplay(timeInterv, time, whatsBeingRecorded, kbUnderstand):
                if whatsBeingRecorded == "Mouse":
                    os.startfile("replayMouse.py")
                elif whatsBeingRecorded == "Keyboard":
                    os.startfile("replayKeyboard.py")
                else:  # KB & M
                    os.startfile("replayMouse.py")
                    os.startfile("replayKeyboard.py")

            if "Unset" in whatsBeingRecorded:
                messagebox.showerror(
                    "Invalid Submission", "Please fill in all the required information correctly.")
            elif whatsBeingRecorded == "Mouse":
                try:
                    # checkMouse()
                    if timeInterv.replace(".", "").isdigit() and time.replace(".", "").isdigit():
                        try:
                            timeInterv = int(timeInterv)
                            time = int(time)
                        except:
                            timeInterv = float(timeInterv)
                            time = float(time)

                        startReplay(timeInterv, time,
                                    whatsBeingRecorded, kbUnderstand)
                    else:
                        messagebox.showerror(
                            "Incorrect Submission.", "Please select valid inputs (numbers).")
                except:
                    pass
            elif whatsBeingRecorded == "Keyboard":
                try:
                    checkKB()
                    if kbUnderstand != "Unset":
                        startReplay(timeInterv, time,
                                    whatsBeingRecorded, kbUnderstand)
                    else:
                        messagebox.showerror(
                            "Incorrect Submission.", "Please fill in all forms correctly.")
                except:
                    pass
            else:  # KB & M
                checkMouse()
                checkKB()
                if kbUnderstand != "Unset" and timeInterv.replace(".", "").isdigit() and time.replace(".", "").isdigit():
                    startReplay(timeInterv, time,
                                whatsBeingRecorded, kbUnderstand)

        empty3 = Label(root, text="", pady=6)
        empty3.pack()

        resetBtn = Button(root, text="Reset", padx=10,
                          pady=5, command=resetScripts)

        resetTxt = Label(root, text="Not working? Click the reset button.")

        global eLoopAmount
        global eRunSpeed

        empty4 = Label(root, text="", pady=4)
        replayBtn = Button(root, text="REPLAY", padx=10,
                           pady=10, command=lambda: REPLAY(eTimeInterval.get(), eTime.get(), whatsBeingRecorded, iUnderstandDropDown.get(), eLoopAmount.get(), eRunSpeed.get()))

        resetBtn.pack()
        resetTxt.pack()

        empty4.pack()
        replayBtn.pack()

        Label(root, text="Replay Settings", pady=7).pack()
        Label(root, text="Replays will run at their recorded settings", pady=0).pack()
        Label(root, text="unless the following settings are changed.", pady=0).pack()
        empty5 = Label(root, text="", pady=5)

        Label(root, text="Loop how many times (default -> 1):", pady=2).pack()
        eLoopAmount = Entry(root)
        eLoopAmount.insert(0, '1')
        eLoopAmount.pack()

        Label(root, text="", pady=3)  # empty

        Label(root, text="Playback speed (default -> 1):", pady=2).pack()
        eRunSpeed = Entry(root)
        eRunSpeed.insert(0, '1')
        eRunSpeed.pack()

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
