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
import matplotlib.pyplot as plt
import ast
import pyautogui


root = Tk()
bgColor = getColor("bg")
textColor = getColor("text")
importDefaultSettings(root)


def startMacro():
    startMacroWindow()


def startRecording():
    startRecordingWindow()


title = Label(root, text="Welcome to vMacro!", padx=10,
              pady=10, bg=bgColor, fg=textColor, font=("Helvetica", 18, "bold"))
subtitle = Label(
    root, text="Would you like to play around with macros or recordings?", padx=5, pady=4, bg=bgColor, fg=textColor, font=("Helvetica", 11)
)

macros = Button(root, text="Macros", padx=10, pady=5,
                command=startMacro, bg=bgColor, fg=textColor, font=("Helvetica", 11, "bold"))
recordings = Button(root, text="Recordings & Replays",
                    padx=10, pady=5, command=startRecording, bg=bgColor, fg=textColor, font=("Helvetica", 11, "bold"))

title.pack()
subtitle.pack()
Label(text="", pady=1, bg=bgColor, fg=textColor).pack()
macros.pack()
recordings.pack()

Label(text="", pady=1, bg=bgColor, fg=textColor).pack()

thisFolder = os.path.dirname(os.path.abspath(
    __file__))

# Graph


def graphMouseData():
    f = open(os.path.join(thisFolder, "logs/mouseMonitor.txt"), "r")
    mouseData = f.read()
    f.close()
    mouseData = ast.literal_eval(mouseData)

    mouseDataX = list(map(list, zip(*mouseData)))[0]
    mouseDataY = list(map(list, zip(*mouseData)))[1]

    fig, ax = plt.subplots()
    scatterPlot = ax.scatter(mouseDataX, mouseDataY, color=textColor)

    resolution = pyautogui.size()
    resolution = list(resolution)

    ax.set_title(
        "Last Mouse Recording's Data Points (Based On Your Cursor Movement)")
    ax.set_xlabel(f"X Coordinates (Your Display: {resolution[0]})")
    ax.set_ylabel(f"Y Coordinates (Your Display: {resolution[1]})")

    plt.axis([0, resolution[0], 0, resolution[1]])
    ax.set_facecolor(bgColor)
    fig.patch.set_facecolor(bgColor)
    ax.spines['bottom'].set_color(textColor)
    ax.spines['top'].set_color(textColor)
    ax.spines['right'].set_color(textColor)
    ax.spines['left'].set_color(textColor)
    ax.tick_params(axis='x', colors=textColor)
    ax.tick_params(axis='y', colors=textColor)
    ax.yaxis.label.set_color(textColor)
    ax.xaxis.label.set_color(textColor)
    ax.title.set_color(textColor)
    plt.show()


gearIcon = ImageTk.PhotoImage(Image.open(
    os.path.join(thisFolder, "img/gearsIconx32.png")))

Button(root, text="Show User Data Graph",
       padx=10, pady=5, command=graphMouseData, bg=bgColor, fg=textColor, font=("Helvetica", 11, "bold")).pack()

Label(text="", pady=0.5, bg=bgColor, fg=textColor).pack()

Button(root, image=gearIcon,
       padx=10, pady=5, command=openSettingsWindow, bg=bgColor, fg=textColor).pack()

Label(text="", pady=0.5, bg=bgColor, fg=textColor).pack()

Label(text="Version: 0.9", pady=0.5, bg=bgColor,
      fg=textColor).pack()

Label(text="© Copyright 2021, Vamiq Valji", pady=0.5, bg=bgColor,
      fg=textColor).pack()


mainloop()
