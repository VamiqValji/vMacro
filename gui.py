from tkinter import *
import os
import asyncio
import time
# from keys import runKeys

root = Tk()

# e = Entry(root, width=50)
# e.grid(row=3, column=0)


def onClick():
    # print("Clicked.")
    # print(e.get())
    try:
        if os.path.exists("keysRunning.txt") == False:
            os.startfile("keys.py")
        else:
            keysRunningLabel.grid(root, row=2, column=0)
        if os.path.exists("mouseRunning.txt") == False:
            os.startfile("mouse.py")
        else:
            mouseRunningLabel.grid(root, row=3, column=0)
    except:
        pass


def amIRecording():
    if os.path.exists("keysRunning.txt") == False:
        return "Not Recording"
    if os.path.exists("mouseRunning.txt") == False:
        return "Recording"


def resetScripts():
    if os.path.exists("keysRunning.txt"):
        os.remove("keysRunning.txt")
    if os.path.exists("mouseRunning.txt"):
        os.remove("mouseRunning.txt")


async def checkKeysRunning():
    while True:
        time.sleep(0.1)
        print("test")

# img
# myImg = ImageTk.PhotoImage(Image.open("/"))

clickMeTxt = Label(root, text="Click me!")
resetTxt = Label(root, text="Not working? Click the reset button.")
status = Label(root, text=amIRecording)
mouseRunningLabel = Label(root, text="Mouse vMacro script is already running.")
keysRunningLabel = Label(
    root, text="Keyboard vMacro script is already running.")

runBtn = Button(root, text="Run", padx=10, pady=5, command=onClick)
resetBtn = Button(root, text="Reset", padx=10, pady=5, command=resetScripts)

clickMeTxt.grid(row=0, column=0)
runBtn.grid(row=1, column=0)
resetBtn.grid(row=4, column=0)
status.grid(row=100, column=0)

root.mainloop()
