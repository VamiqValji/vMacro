import time
import os
from os import listdir
from os.path import isfile, join
import pynput
from pynput.keyboard import Key, Listener, Controller
import sys


def replayKB(keysPressedList, loopAmount, replaySpeed):
    loopAmount = float(loopAmount)
    replaySpeed = float(replaySpeed)
    print(f"\n\n{keysPressedList}\n\n")
    keyboard = Controller()
    keysPressedList = keysPressedList * int(round(loopAmount, 0))
    for k in keysPressedList:
        try:
            if keysPressedList.index(k) < len(keysPressedList):
                k = keysPressedList.index(k) * 2
                if keysPressedList[k] != "wait":
                    keyboard.press(keysPressedList[k])
                time.sleep(
                    (float(keysPressedList[k + 1]) / 3) / replaySpeed)
                if keysPressedList[k] != "wait":
                    keyboard.release(keysPressedList[k])
        except:
            sys.exit()
            break


def getInfo():

    thisFolder = os.path.dirname(os.path.abspath(
        __file__)) + f"/logs/"
    my_file = os.path.join(thisFolder, "keysPressed.txt")

    # Get list of keys pressed
    f = open(my_file)
    keysPressed = f.read()
    f.close()

    keysPressedList = keysPressed.split(",")

    # Get replay settings
    my_file = os.path.join(thisFolder, "replaySettings.txt")
    f = open(my_file, "r")
    replaySett = f.readlines()
    f.close()

    my_file = os.path.join(thisFolder, "delay.txt")
    f = open(my_file, "r")
    delay = f.read()
    f.close()
    delay = float(delay)

    loopAmount = replaySett[0]
    replaySpeed = replaySett[1]

    if delay > 0:
        print("\nWaiting...")
        time.sleep(delay)

    # Start Replay
    replayKB(keysPressedList, loopAmount, replaySpeed)


getInfo()

# with Listener() as listener:
#     listener.join()  # loop until broken out
