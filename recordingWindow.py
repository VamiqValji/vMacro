from tkinter import *
from tkinter import messagebox
import os
from os import listdir
from os.path import isfile, join
import asyncio
import time
from profilesWindow import openProfilesWindow
from replaySettingsWindow import getInfo
from defaultSettings import importDefaultSettings
from defaultSettings import getColor


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
        bgColor = getColor("bg")
        textColor = getColor("text")
        importDefaultSettings(root)

        title = Label(
            root, text=f"Record: {whatsBeingRecorded}", pady="10", padx="5", bg=bgColor, fg=textColor)
        title.pack()

        global eTimeInterval
        global eTime
        global eRecordingAndReplayDelay
        eTimeInterval = Entry(root, bg=bgColor, fg=textColor)
        eTime = Entry(root, bg=bgColor, fg=textColor)
        eRecordingAndReplayDelay = Entry(root, bg=bgColor, fg=textColor)
        eTimeInterval.insert(0, '0.1')
        eTime.insert(0, '1')
        eRecordingAndReplayDelay.insert(0, '0')

        global moveToEnd
        moveToEnd = StringVar()
        moveToEnd.set("Manually Close To End Replay")

        def renderRecordBtn():
            Button(root, text="Start Recording",
                   padx=10, pady=10, command=lambda: RECORD(eTimeInterval.get(), eTime.get(), iUnderstandDropDown.get(), eRecordingAndReplayDelay.get()), bg=bgColor, fg=textColor).pack()

        def renderMouseSettings():

            mouseSettingsTitle = Label(
                root, text="Mouse Settings", pady="12", padx="5", bg=bgColor, fg=textColor)
            mouseSettingsTitle.pack()
            instructionsTxtMouse = Label(
                root, text="To end the mouse recording once its started, move your mouse.", pady="8", padx="5", bg=bgColor, fg=textColor)
            intervalTxt1 = Label(
                root, text="Enter a time interval for mouse tracking (seconds);", pady="0", padx="5", bg=bgColor, fg=textColor)
            intervalTxt2 = Label(
                root, text="the lower the number, the smoother the tracking.", pady="0", padx="5", bg=bgColor, fg=textColor)
            intervalTxt3 = Label(
                root, text="Enter the amount of time the mouse will be tracked (seconds)", pady="8", padx="5", bg=bgColor, fg=textColor)
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
            Label(root, text="", pady=3, bg=bgColor, fg=textColor).pack()
            if whatsBeingRecorded == "Mouse":
                renderRecordBtn()

        global iUnderstandDropDown
        iUnderstandDropDown = StringVar()
        iUnderstandDropDown.set("Unset")

        def renderKBSettings():
            KBSettingsTitle = Label(
                root, text="Keyboard Settings", pady="12", padx="5", bg=bgColor, fg=textColor)
            instructionsTxtKB1 = Label(
                root, text="To end the keyboard recording", pady="4", padx="5", bg=bgColor, fg=textColor)
            instructionsTxtKB2 = Label(
                root, text="once its started, hit escape.", pady="0", padx="5", bg=bgColor, fg=textColor)

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

        empty3 = Label(root, text="", pady=6, bg=bgColor, fg=textColor)
        empty3.pack()

        intervalTxt4 = Label(
            root, text="Enter the amount of time the recording and replay will start after (delay).", pady="8", padx="5", bg=bgColor, fg=textColor)
        intervalTxt4.pack()
        eRecordingAndReplayDelay.pack()
        Label(root, text="", pady=3, bg=bgColor, fg=textColor).pack()

        # resetBtn = Button(root, text="Reset", padx=10,
        #                   pady=5, command=resetScripts)

        # resetTxt = Label(root, text="Not working? Click the reset button.")

        global eLoopAmount
        global eRunSpeed

        empty4 = Label(root, text="", pady=4, bg=bgColor, fg=textColor)
        replayBtn = Button(root, text="REPLAY", padx=10,
                           pady=10, command=lambda: REPLAY(eTimeInterval.get(), eTime.get(), whatsBeingRecorded, iUnderstandDropDown.get(), eLoopAmount.get(), eRunSpeed.get(), moveToEnd.get()), bg=bgColor, fg=textColor)

        # resetBtn.pack()
        # resetTxt.pack()

        empty4.pack()
        replayBtn.pack()

        Label(root, text="Replay Settings", pady=7,
              bg=bgColor, fg=textColor).pack()
        Label(root, text="Replays will run at their recorded settings",
              pady=0, padx=3, bg=bgColor, fg=textColor).pack()
        Label(root, text="unless the following settings are changed.",
              pady=0, padx=3, bg=bgColor, fg=textColor).pack()

        empty5 = Label(root, text="", pady=5, bg=bgColor, fg=textColor)
        Label(root, text="", pady=1, bg=bgColor, fg=textColor).pack()
        if whatsBeingRecorded != "Mouse" and whatsBeingRecorded != "Unset":
            Label(root, text="RECOMMENDED:", pady=1,
                  bg=bgColor, fg=textColor).pack()
            Label(root, text="Click the button below to make sure",
                  pady=1, bg=bgColor, fg=textColor).pack()
            Label(root, text="your keyboard script is exactly how",
                  pady=1, bg=bgColor, fg=textColor).pack()
            Label(root, text="you want it.", pady=1,
                  bg=bgColor, fg=textColor).pack()
            Button(root, text="Open Keyboard Replay Script", pady=0,
                   padx=3, command=getInfo, bg=bgColor, fg=textColor).pack()  # starts replaySettingsWindow

            Label(root, text="", pady=1, bg=bgColor, fg=textColor).pack()

        Label(root, text="Loop how many times (default -> 1):",
              pady=2, bg=bgColor, fg=textColor).pack()
        eLoopAmount = Entry(root, bg=bgColor, fg=textColor)
        eLoopAmount.insert(0, '1')
        eLoopAmount.pack()

        Label(root, text="", pady=3, bg=bgColor, fg=textColor)  # empty

        Label(root, text="Playback speed (default -> 1):",
              pady=2, bg=bgColor, fg=textColor).pack()
        eRunSpeed = Entry(root, bg=bgColor, fg=textColor)
        eRunSpeed.insert(0, '1')
        eRunSpeed.pack()

        empty5.pack()

        mainloop()

    root = Tk()
    bgColor = getColor("bg")
    textColor = getColor("text")
    importDefaultSettings(root)

    title = Label(
        root, text="Recordings", pady="10", padx="5", bg=bgColor, fg=textColor)
    title.grid(row=0, column=0)
    instructions = Label(
        root, text="Choose What To Record:", pady="4", padx="5", bg=bgColor, fg=textColor)

    # status = Label(root, text="Not Recording",  bd=1, relief=SUNKEN)

    dropDown = StringVar()
    dropDown.set("Unset")
    inpFieldDrop = OptionMenu(
        root, dropDown, *["Record Mouse", "Record Keyboard [EXPERIMENTAL]", "Record Mouse & KB [EXPERIMENTAL]"])
    openRecordingBtn = Button(
        root, text="Open Recording Window", padx=10, pady=5, command=lambda: actualRecordingWindow(dropDown.get()), bg=bgColor, fg=textColor)

    empty = Label(
        root, text="", bg=bgColor, fg=textColor)

    instructions.grid(row=1, column=0, padx=5, pady=5)
    inpFieldDrop.grid(row=2, column=0, padx=5, pady=5)
    openRecordingBtn.grid(row=3, column=0, padx=5, pady=5)
    empty.grid(row=4, column=0, padx=5, pady=1)

    # root.mainloop()

    mainloop()


# startRecordingWindow()
