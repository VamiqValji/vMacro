import os
from pynput.keyboard import Key, Listener, Controller
from pynput.mouse import Button, Controller, Listener
from pynput import mouse
import time

mouse = Controller()

mouseMonitorList = []

recordingMouse = True
replayRunning = True

replayTimeCounter = 0

timeInterval = 0.05
maxTime = 3


def clearRunningScripts():
    try:
        if os.path.exists("../vMacro/logs/keysRunning.txt"):
            os.remove("../vMacro/logs/keysRunning.txt")
        if os.path.exists("../vMacro/logs/mouseRunning.txt"):
            os.remove("../vMacro/logs/mouseRunning.txt")
    except:
        pass


def mouseRecord(timeIntervalArg, timeArg, delay):
    global mouseMonitorList
    global recordingMouse
    global replayTimeCounter
    global timeInterval
    global maxTime
    replayTimeCounter = 0
    timeInterval = float(timeIntervalArg)
    maxTime = float(timeArg)
    delay = float(delay)
    timeCounter = 0
    if delay > 0:
        print("\nWaiting...")
        time.sleep(delay)
    while recordingMouse:
        if timeCounter < maxTime:
            timeCounter += timeInterval
            print(mouse.position)
            mouseMonitorList.append(mouse.position)
            time.sleep(timeInterval)
        else:
            writeMouse()
            # replayMouse()
            recordingMouse = False


def writeMouse():
    f = open("../vMacro/logs/mouseMonitor.txt", "w")
    f.write(str(mouseMonitorList))
    f.close()


def startMouseRecord():

    clearRunningScripts()
    print("\n\n\nMove your mouse to exit!\n\nStarting vMacro (Mouse).\n")

    thisFolder = os.path.dirname(os.path.abspath(
        __file__)) + f"/logs/"

    my_file = os.path.join(thisFolder, "mouseRunning.txt")
    f = open(my_file, "w")
    f.write("Running")
    f.close()

    my_file = os.path.join(thisFolder, "mouseRunSettings.txt")
    f = open(my_file, "r")
    mouseSettings = f.readlines()
    f.close()

    my_file = os.path.join(thisFolder, "delay.txt")
    f = open(my_file, "r")
    delay = f.read()
    f.close()

    timeInterv = mouseSettings[0]
    time = mouseSettings[1]

    mouseRecord(timeInterv, time, delay)


startMouseRecord()
