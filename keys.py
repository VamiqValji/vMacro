import time
import os
import pynput
from pynput.keyboard import Key, Listener, Controller

keyboard = Controller()

keysPressedList = []

startTime = time.time()
print(startTime)

print("\n\n\nHit escape to exit!\n\nStarting vMacro.\n")

pressed = False
replaying = False


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
    if replaying == False:
        pressed = True
        if pressed == False:
            print(f"{key} pressed.")
            startCounter()
        else:
            print(f"{key} held down.")
    if key == Key.enter:
        pressed = False
        if replaying == False:
            replay()
            return False


def replay():
    global keysPressedList
    global replaying
    replaying = True
    # writeFile()
    # os.startfile("keysPressed.txt")
    makeEven = 1
    for k in keysPressedList:
        try:
            print(f"\n\n-REPLAY-\n")
            if k % 2 != 0:
                makeEven = k - 1
            k = keysPressedList.index(k) * 2
            keyboard.press(keysPressedList[makeEven])
            print(f"{keysPressedList[makeEven]} being pressed.")
            time.sleep(1)
            print(f"Waiting {keysPressedList[k + 1]} seconds.")
            keyboard.release(keysPressedList[makeEven])
            print(f"{keysPressedList[makeEven]} released.")
            if (keysPressedList.index(k) / 2 == len(keysPressedList)):
                keyboard.release(keysPressedList[makeEven])
                print("\nMacro Complete.\n")
                return False
        except:
            pass


def on_release(key):
    global keysPressedList
    global replaying
    if key == Key.esc:
        print("\nExited vMacro.\n")
        writeFile()
        os.startfile("keysPressed.txt")
        return False  # break out of loop
    else:
        if replaying == False:
            keysPressedList.append(key)
            keysPressedList.append(f"{round(stopCounter(), 2)}")
            print(f"{key} released.")


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # loop until broken out
