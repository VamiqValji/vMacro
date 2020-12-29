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


def replay():
    global keysPressedList
    global replaying
    replaying = True
    writeFile()
    os.startfile("keysPressed.txt")
    for k in keysPressedList:
        k = keysPressedList.index(k) * 2
        # print("\n\nfirst" + keysPressedList[k + 1])
        # start = time.time()
        keyboard.press(keysPressedList[k])
        # print("\n\nsecond" + keysPressedList[k + 1])
        # print(keysPressedList[k])
        time.sleep(float(keysPressedList[k + 1]))
        # time.sleep(1)
        # print("\n\nthird" + keysPressedList[k + 1])
        # print("Start Loop.")
        # while True:
        #     print("Looping.")
        #     if time.time() == start + keysPressedList[k + 1]:
        keyboard.release(keysPressedList[k])
        #         print("End Loop.")
        #         return False
        # print("\n\nfourth" + keysPressedList[k + 1])


def on_release(key):
    global keysPressedList
    global replaying
    if key == Key.esc:
        print("\nExited vMacro.\n")
        writeFile()
        os.startfile("keysPressed.txt")
        return False  # break out of loop
    elif key == Key.enter:
        if replaying == False:
            replay()
    else:
        if replaying == False:
            keysPressedList.append(key)
            keysPressedList.append(f"{round(stopCounter(), 2)}")
            print(f"{key} released.")


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # loop until broken out
