import time
import os
from os import listdir
from os.path import isfile, join
import pynput
from pynput.keyboard import Key, Listener, Controller
import sys


def replayKB(keysPressedList, loopAmount, replaySpeed):

    loop = 0
    loopAmount = float(loopAmount)
    replaySpeed = float(replaySpeed)

    print(f"\n\n{keysPressedList}\n\n")
    keyboard = Controller()
    while loop < loopAmount:
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
                loop += 1
                if loop >= loopAmount:
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

    loopAmount = replaySett[0]
    replaySpeed = replaySett[1]

    # Start Replay
    replayKB(keysPressedList, loopAmount, replaySpeed)


getInfo()


# with Listener() as listener:
#     listener.join()  # loop until broken out
