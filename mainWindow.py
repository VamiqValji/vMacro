from tkinter import *
import os
from os import listdir
from os.path import isfile, join
import asyncio
import time
from macroWindow import startMacroWindow
from recordingWindow import startRecordingWindow

root = Tk()
root.title("vMacro")


def startMacro():
    startMacroWindow()


def startRecording():
    startRecordingWindow()


title = Label(root, text="Welcome to vMacro!", padx=10, pady=10)
subtitle = Label(
    root, text="Would you like to play around with macros or recordings?", padx=0, pady=4)

macros = Button(root, text="Macros", padx=10, pady=5, command=startMacro)
recordings = Button(root, text="Recordings (Experimental)",
                    padx=10, pady=5, command=startRecording)

title.pack()
subtitle.pack()
macros.pack()
recordings.pack()

mainloop()
