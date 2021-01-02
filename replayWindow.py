from tkinter import *
from tkinter import messagebox
import os
from os import listdir
from os.path import isfile, join

counter = 0


def REPLAY(timeInterv, time, whatsBeingRecorded, kbUnderstand):
    print("\nReplay")

    replayTimeCounter = 0
    timeInterval = timeInterv
    maxTime = time

    for mousePos in mouseMonitorList:
        if replayTimeCounter <= maxTime:
            mouse.position = mousePos
            replayTimeCounter = round(
                replayTimeCounter, 1) + round(timeInterval, 1)
            time.sleep(timeInterval)
            if replayTimeCounter > maxTime:
                print("Mouse click.")
                mouse.click(Button.left, 2)
                clearRunningScripts()


def getInfo():
    f = open("..vMacro/logs/replaySettings.txt", "r")
    readlines = f.readlines()
    f.close()

    timeInterv = readlines[0]
    time = readlines[1]
    whatsBeingRecorded = readlines[2]
    kbUnderstand = readlines[3]

    REPLAY(timeInterv, time, whatsBeingRecorded, kbUnderstand)
