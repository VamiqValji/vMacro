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
from defaultSettings import getColor
from PIL import ImageTk, Image

root = Tk()
bgColor = getColor("bg")
textColor = getColor("text")
importDefaultSettings(root)


def startMacro():
    startMacroWindow()


def startRecording():
    startRecordingWindow()


title = Label(root, text="Welcome to vMacro!", padx=10,
              pady=10, bg=bgColor, fg=textColor)
subtitle = Label(
    root, text="Would you like to play around with macros or recordings?", padx=0, pady=4, bg=bgColor, fg=textColor)

macros = Button(root, text="Macros", padx=10, pady=5,
                command=startMacro, bg=bgColor, fg=textColor)
recordings = Button(root, text="Recordings (Experimental)",
                    padx=10, pady=5, command=startRecording, bg=bgColor, fg=textColor)

title.pack()
subtitle.pack()
macros.pack()
recordings.pack()

Label(text="", pady=1, bg=bgColor, fg=textColor).pack()
# Button(root, text="Settings",
#        padx=10, pady=5, command=openSettingsWindow).pack()

# Image
thisFolder = os.path.dirname(os.path.abspath(
    __file__)) + f"/img/"

gearIcon = ImageTk.PhotoImage(Image.open(
    os.path.join(thisFolder, "gearsIconx32.png")))

Button(root, image=gearIcon,
       padx=10, pady=5, command=openSettingsWindow, bg=bgColor, fg=textColor).pack()

#

Label(text="", pady=0.5, bg=bgColor, fg=textColor).pack()


mainloop()
