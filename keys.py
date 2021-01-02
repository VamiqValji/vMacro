import time
import os
from os import listdir
from os.path import isfile, join
import pynput
from pynput.keyboard import Key, Listener, Controller
import sys
# from mouse import *

keyboard = Controller()

keysPressedList = []

startTime = time.time()
noKeyPressedTime = time.time()
pressed = False
replaying = False
appendCount = 0


def clearRunningScripts():
    # path = os.path.dirname(os.path.abspath(__file__))
    # # joins path of all files in directory
    # files = [f for f in listdir(path)
    #          if isfile(join(path, f))]
    # for file in files:
    #     if "Running" in file:
    #         print(file)
    #         with open(file) as f:
    #             os.remove(file)
    try:
        if os.path.exists("../vMacro/logs/keysRunning.txt"):
            f = open("../vMacro/logs/keysPressed.txt", "r")
            fp = open("../vMacro/logs/keysPressed_prev_log.txt", "w")
            fp.write(f.read())
            f.close()
            fp.close()
            os.remove("../vMacro/logs/keysRunning.txt")
        if os.path.exists("mouseRunning.txt"):
            os.remove("../vMacro/logs/mouseRunning.txt")
    except:
        pass


def writeFile():
    f = open("../vMacro/logs/keysPressed.txt", "w")
    keysPressedStr = ""
    print(keysPressedList)
    for keyPressed in keysPressedList:
        if "Key" in (f"{keyPressed}"):
            keyPressed = f",{keyPressed},"
        keysPressedStr += f"'{keyPressed}'"
    keysPressedStr = ((keysPressedStr.replace(
        "'''", ",")).strip("''")).replace("'", "").replace("wait", ",wait,")
    if keysPressedStr[1:5] == "wait":
        keysPressedStr = keysPressedStr[1:]
    f.write(keysPressedStr)
    f.close()


def startCounter():
    global startTime
    startTime = time.time()


def stopCounter():
    global pressed
    global startTime
    pressed = False
    endTime = startTime
    startTime = time.time()
    return time.time() - endTime


def on_press(key):
    global pressed
    global replaying
    global keysPressedList
    global noKeyPressedTime
    global appendCount
    if replaying == False:
        pressed = True
        if pressed == False:
            print(f"{key} pressed.")
            startCounter()
        else:
            print(f"{key} held down.")


def replayKB():
    global keysPressedList
    print(f"\n\n{keysPressedList}\n\n")
    while True:
        for k in keysPressedList:
            try:
                if keysPressedList.index(k) < len(keysPressedList):
                    k = keysPressedList.index(k) * 2
                    if keysPressedList[k] != "wait":
                        keyboard.press(keysPressedList[k])
                    time.sleep(float(keysPressedList[k + 1]) / 3)
                    if keysPressedList[k] != "wait":
                        keyboard.release(keysPressedList[k])
            except:
                print("done")
                clearRunningScripts()
                sys.exit()
                break


def on_release(key):
    global keysPressedList
    # global replaying
    global noKeyPressedTime
    global pressed
    pressed = False
    noKeyPressedTime = time.time() - noKeyPressedTime
    keysPressedList.append("wait")
    keysPressedList.append(f"{round(noKeyPressedTime,2)}")
    noKeyPressedTime = time.time()  # reset
    if key == Key.esc:
        print("\nExited vMacro.\n")
        writeFile()
        os.startfile("../vMacro/logs/keysPressed.txt")
        clearRunningScripts()
        return False  # break out of loop
    # elif key == Key.enter:
    #     if replaying == False:
    #         replayKB()
    #         replaying = True
    else:
        if replaying == False:
            keysPressedList.append(key)
            keysPressedList.append(f"{round(stopCounter(), 2)}")
            print(f"{key} released.")


def startKBRecord():
    clearRunningScripts()
    print("\n\n\nHit escape to exit! Hit enter to replay!\n\nStarting vMacro (Keyboard - RECORDING).\n")

    f = open("../vMacro/logs/keysRunning.txt", "w")
    f.write("Running")
    f.close()

    # start


startKBRecord()


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # loop until broken out
