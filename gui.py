from tkinter import *
import os
import asyncio
import time
# from keys import runKeys

root = Tk()

e = Entry(root, width=50)
e.grid(row=3, column=0)


def onClick():
    # print("Clicked.")
    # print(e.get())
    try:
        if os.path.exists("keysRunning.txt") == False:
            os.startfile("keys.py")
        else:
            keysRunningLabel.pack()
        if os.path.exists("mouseRunning.txt") == False:
            os.startfile("mouse.py")
        else:
            mouseRunningLabel.pack()
    except:
        pass


async def checkKeysRunning():
    while True:
        time.sleep(0.1)
        print("test")


myLabel1 = Label(root, text="Click me!")
btn1 = Button(root, text="test", padx=10, pady=5, command=onClick)

mouseRunningLabel = Label(root, text="Mouse vMacro script is already running.")
keysRunningLabel = Label(
    root, text="Keyboard vMacro script is already running.")

myLabel1.grid(row=0, column=0)
btn1.grid(row=1, column=0)

root.mainloop()
