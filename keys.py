import pynput
from pynput.keyboard import Key, Listener

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
    global keysPressedList
    keysPressedList.append(key)
    print(f"{key} pressed.")


def on_release(key):
    if key == Key.esc:
        print("\nExited vMacro.\n")
        writeFile()
        return False  # break out of loop
    print(f"{key} released.")


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # loop until broken out
