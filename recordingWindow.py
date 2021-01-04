from tkinter import *
from tkinter import messagebox
import os
from os import listdir
from os.path import isfile, join
import asyncio
import time
from profilesWindow import openProfilesWindow
from replaySettingsWindow import getInfo


def startRecordingWindow():

    def resetScripts():
        try:
            if os.path.exists("../vMacro/logs/keysRunning.txt"):
                os.remove("../vMacro/logs/keysRunning.txt")
            if os.path.exists("../vMacro/logs/mouseRunning.txt"):
                os.remove("../vMacro/logs/mouseRunning.txt")
        except:
            pass

    def actualRecordingWindow(whatsBeingRecorded):

        whatsBeingRecorded = whatsBeingRecorded.replace("Record ", "")

        def RECORD(timeInterv, time, kbUnderstand, RRdelay):

            resetScripts()

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

            if RRdelay.replace(".", "").isdigit():
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
                fR = open("../vMacro/logs/delay.txt", "w")
                fR.write(RRdelay)
                fR.close()
            else:
                messagebox.showerror(
                    "Incorrect Submission.", "Your inputted recording and replay delay must be a valid number.")

        root = Tk()
        root.title("vMacro")

        title = Label(
            root, text=f"Record: {whatsBeingRecorded}", pady="10", padx="5")
        title.pack()

        global eTimeInterval
        global eTime
        global eRecordingAndReplayDelay
        eTimeInterval = Entry(root)
        eTime = Entry(root)
        eRecordingAndReplayDelay = Entry(root)
        eTimeInterval.insert(0, '0.1')
        eTime.insert(0, '1')
        eRecordingAndReplayDelay.insert(0, '0')

        global moveToEnd
        moveToEnd = StringVar()
        moveToEnd.set("Manually Close To End Replay")

        def renderRecordBtn():
            Button(root, text="Start Recording",
                   padx=10, pady=10, command=lambda: RECORD(eTimeInterval.get(), eTime.get(), iUnderstandDropDown.get(), eRecordingAndReplayDelay.get())).pack()

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
            # intervalTxt4 = Label(
            #     root, text="Enter the amount of time the recording and replay will start after (delay).", pady="8", padx="5")
            instructionsTxtMouse.pack()
            intervalTxt1.pack()
            intervalTxt2.pack()
            eTimeInterval.pack()
            intervalTxt3.pack()
            eTime.pack()
            # intervalTxt4.pack()
            # eRecordingAndReplayDelay.pack()
            # Label(root, text="", pady=3).pack()
            OptionMenu(
                root, moveToEnd, *["Manually Close To End Replay", "Move Mouse to End Replay"]).pack()
            Label(root, text="", pady=3).pack()
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

        def REPLAY(timeInterv, time, whatsBeingRecorded, kbUnderstand, loopAmount, runSpeed, endMethod):

            thisFolder = os.path.dirname(os.path.abspath(
                __file__)) + f"/logs/"

            if loopAmount.replace(".", "").isdigit() and runSpeed.replace(".", "").isdigit():
                if endMethod == "Manually Close To End Replay":
                    endMethod = "1"
                elif endMethod == "Move Mouse to End Replay":
                    endMethod = "2"

                f = open("../vMacro/logs/replaySettings.txt", "w")
                f.write(f"{loopAmount}\n{runSpeed}\n{endMethod}")
                f.close()
            else:
                return messagebox.showerror(
                    "Invalid Submission", "Please fill in all the required information correctly.")

            def checkMouse():
                my_file = os.path.join(thisFolder, "mouseMonitor.txt")
                fM = open(my_file)
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

        intervalTxt4 = Label(
            root, text="Enter the amount of time the recording and replay will start after (delay).", pady="8", padx="5")
        intervalTxt4.pack()
        eRecordingAndReplayDelay.pack()
        Label(root, text="", pady=3).pack()

        # resetBtn = Button(root, text="Reset", padx=10,
        #                   pady=5, command=resetScripts)

        # resetTxt = Label(root, text="Not working? Click the reset button.")

        global eLoopAmount
        global eRunSpeed

        empty4 = Label(root, text="", pady=4)
        replayBtn = Button(root, text="REPLAY", padx=10,
                           pady=10, command=lambda: REPLAY(eTimeInterval.get(), eTime.get(), whatsBeingRecorded, iUnderstandDropDown.get(), eLoopAmount.get(), eRunSpeed.get(), moveToEnd.get()))

        # resetBtn.pack()
        # resetTxt.pack()

        empty4.pack()
        replayBtn.pack()

        Label(root, text="Replay Settings", pady=7).pack()
        Label(root, text="Replays will run at their recorded settings",
              pady=0, padx=3).pack()
        Label(root, text="unless the following settings are changed.",
              pady=0, padx=3).pack()

        empty5 = Label(root, text="", pady=5)
        Label(root, text="", pady=1).pack()
        if whatsBeingRecorded != "Mouse" and whatsBeingRecorded != "Unset":
            Label(root, text="RECOMMENDED:", pady=1).pack()
            Label(root, text="Click the button below to make sure", pady=1).pack()
            Label(root, text="your keyboard script is exactly how", pady=1).pack()
            Label(root, text="you want it.", pady=1).pack()
            Button(root, text="Open Keyboard Replay Script", pady=0,
                   padx=3, command=getInfo).pack()  # starts replaySettingsWindow

            Label(root, text="", pady=1).pack()

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
