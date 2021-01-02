import os
from os import listdir
from os.path import isfile, join
from pynput.mouse import Button, Controller, Listener
from pynput import mouse
import ast
import time


def replayMouse(timeInterv, mTime, mouseMonitorList, loopAmount, replaySpeed):
    print("\nReplay")
    replayTimeCounter = 0
    loop = 0
    timeInterval = float(timeInterv)
    maxTime = float(mTime)
    loopAmount = float(loopAmount)
    replaySpeed = float(replaySpeed)
    mouse = Controller()
    while loop < loopAmount:
        if replayTimeCounter <= maxTime:
            for mousePos in mouseMonitorList:
                mouse.position = mousePos
                # replayTimeCounter = round(
                #     replayTimeCounter, 1) + round(timeInterval, 1)
                replayTimeCounter += timeInterval * 2
                print(replayTimeCounter)
                time.sleep(timeInterval / replaySpeed)
            if replayTimeCounter > maxTime:
                if loop < loopAmount:
                    replayTimeCounter = 0
                print("Mouse click.")
                mouse.click(Button.left, 2)
                # clearRunningScripts()
            loop += 1


def getInfo():
    thisFolder = os.path.dirname(os.path.abspath(
        __file__)) + f"/logs/"
    my_file = os.path.join(thisFolder, "mouseRunSettings.txt")
    f = open(my_file, "r")
    readlines = f.readlines()
    f.close()

    timeInterv = readlines[0]
    mTime = readlines[1]
    # whatsBeingRecorded = readlines[2]
    # kbUnderstand = readlines[3]

    my_file = os.path.join(thisFolder, "mouseMonitor.txt")
    f = open(my_file, "r")
    mousePositions = f.read()
    f.close()

    mousePositionsList = ast.literal_eval(mousePositions)
    # turns string list (mousePositions) into an actual list

    my_file = os.path.join(thisFolder, "replaySettings.txt")
    f = open(my_file, "r")
    replaySett = f.readlines()
    f.close()

    loopAmount = replaySett[0]
    replaySpeed = replaySett[1]

    replayMouse(timeInterv, mTime, mousePositionsList, loopAmount, replaySpeed)


getInfo()
