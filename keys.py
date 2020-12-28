import pynput
from pynput.keyboard import Key, Listener, Controller

keyboard = Controller()

keysPressedList = []

print("\n\n\nHit escape to exit!\n\nStarting vMacro.\n")


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


def on_press(key):

    print(f"{key} pressed.")


def on_release(key):
    global keysPressedList
    if key == Key.esc:
        print("\nExited vMacro.\n")
        writeFile()
        return False  # break out of loop
    elif key == Key.enter:
        for k in keysPressedList:
            keyboard.press(k)
            keyboard.release(k)
    else:
        keysPressedList.append(key)
        print(f"{key} released.")


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # loop until broken out
