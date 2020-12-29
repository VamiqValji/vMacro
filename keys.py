import time
import pynput
from pynput.keyboard import Key, Listener, Controller

keyboard = Controller()

keysPressedList = []

startTime = time.time()
print(startTime)

print("\n\n\nHit escape to exit!\n\nStarting vMacro.\n")

pressed = False


def writeFile():
    f = open("keysPressed.txt", "w")
    keysPressedStr = ""
    print(keysPressedList)
    for keyPressed in keysPressedList:
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
    pressed = True
    if pressed == False:
        print(f"{key} pressed.")
        startCounter()
    else:
        print(f"{key} held down.")


def replay():
    global keysPressedList
    for k in keysPressedList:
        keyboard.press(k)
        time.sleep(0.3)
        keyboard.release(k)


def on_release(key):
    global keysPressedList
    if key == Key.esc:
        print("\nExited vMacro.\n")
        writeFile()
        return False  # break out of loop
    elif key == Key.enter:
        replay()
    else:
        keysPressedList.append(key)
        keysPressedList.append(f"{round(stopCounter(), 2)}")
        print(f"{key} released.")


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # loop until broken out
