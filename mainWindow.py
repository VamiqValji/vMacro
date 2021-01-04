from tkinter import *
import os
from os import listdir
from os.path import isfile, join
import asyncio
import time
from macroWindow import startMacroWindow
from recordingWindow import startRecordingWindow
from settingsWindow import openSettingsWindow
from defaultSettings import importDefaultSettings
from PIL import ImageTk, Image

root = Tk()
importDefaultSettings(root)


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

Label(text="", pady=1).pack()
# Button(root, text="Settings",
#        padx=10, pady=5, command=openSettingsWindow).pack()

# Image
thisFolder = os.path.dirname(os.path.abspath(
    __file__)) + f"/img/"

gearIcon = ImageTk.PhotoImage(Image.open(
    os.path.join(thisFolder, "gearsIconx32.png")))

Button(root, image=gearIcon,
       padx=10, pady=5, command=openSettingsWindow).pack()

#

Label(text="", pady=0.5).pack()


mainloop()
