import os
from os import listdir
from os.path import isfile, join
from pynput.mouse import Button, Controller, Listener
from pynput import mouse
import ast
import time
import sys


def replayMouse(timeInterv, mTime, mouseMonitorList, loopAmount, replaySpeed, endMethod, delay):
    print("\nReplay")
    replayTimeCounter = 0
    loop = 0
    prevPos = 0
    timeInterval = float(timeInterv)
    maxTime = float(mTime)
    loopAmount = float(loopAmount)
    replaySpeed = float(replaySpeed)
    endMethod = int(endMethod)
    delay = float(delay)
    mouse = Controller()

    if delay > 0:
        print("\nWaiting...")
        time.sleep(delay)

    while loop < loopAmount:
        if replayTimeCounter <= maxTime:
            for mousePos in mouseMonitorList:
                mouse.position = mousePos
                if endMethod == 2:
                    prevPos = mouse.position
                replayTimeCounter += timeInterval * 2
                print(replayTimeCounter)
                time.sleep(timeInterval / replaySpeed)
                if endMethod == 2 and mouse.position != prevPos:
                    sys.exit()
                    break
            if replayTimeCounter > maxTime:
                if loop < loopAmount:
                    replayTimeCounter = 0
                # print("Mouse click.")
                # mouse.click(Button.left, 2)
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
    endMethod = replaySett[2]

    my_file = os.path.join(thisFolder, "delay.txt")
    f = open(my_file, "r")
    delay = f.read()
    f.close()

    replayMouse(timeInterv, mTime, mousePositionsList,
                loopAmount, replaySpeed, endMethod, delay)


getInfo()
