import time
import os
import pynput
from pynput.keyboard import Key, Listener, Controller
# from mouse import *

keyboard = Controller()

keysPressedList = []

startTime = time.time()
noKeyPressedTime = time.time()
pressed = False
replaying = False
appendCount = 0

print("\n\n\nHit escape to exit!\n\nStarting vMacro.\n")


def writeFile():
    f = open("keysPressed.txt", "w")
    keysPressedStr = ""
    print(keysPressedList)
    for keyPressed in keysPressedList:
        if "Key" in (f"{keyPressed}"):
            keyPressed = f",{keyPressed},"
        keysPressedStr += f"'{keyPressed}'"
    keysPressedStr = ((keysPressedStr.replace(
        "'''", ",")).strip("''")).replace("'", "")
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
    # if appendCount > 0:
    #     keysPressedList.append(f", ,")
    #     appendCount += 1
    # else:
    #     keysPressedList.append(f" ,")

    if replaying == False:
        pressed = True
        if pressed == False:
            print(f"{key} pressed.")
            startCounter()
        else:
            print(f"{key} held down.")


def replay():
    global keysPressedList
    # writeFile()
    # os.startfile("keysPressed.txt")
    print(f"\n\n{keysPressedList}\n\n")
    while True:
        for k in keysPressedList:
            if keysPressedList.index(k) < len(keysPressedList):
                k = keysPressedList.index(k) * 2
                if keysPressedList[k] != "wait":
                    keyboard.press(keysPressedList[k])
                time.sleep(float(keysPressedList[k + 1]) / 3)
                if keysPressedList[k] != "wait":
                    keyboard.release(keysPressedList[k])
            else:
                break


def on_release(key):
    global keysPressedList
    global replaying
    global noKeyPressedTime
    global pressed
    pressed = False
    noKeyPressedTime = time.time() - noKeyPressedTime
    keysPressedList.append("wait")
    keysPressedList.append(f"{round(noKeyPressedTime,2)}")
    noKeyPressedTime = time.time()  # reset
    if key == Key.esc:
        print("\nExited vMacro.\n")
        # mouseScriptRunning = False
        writeFile()
        os.startfile("keysPressed.txt")
        return False  # break out of loop
    elif key == Key.enter:
        if replaying == False:
            replay()
            replaying = True
    else:
        if replaying == False:
            keysPressedList.append(key)
            keysPressedList.append(f"{round(stopCounter(), 2)}")
            print(f"{key} released.")


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # loop until broken out
