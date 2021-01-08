import sys
from pynput.keyboard import Key, Listener, Controller
import pynput
import os
import time
from os import listdir
from os.path import isfile, join
import pyautogui
# import pyautogui


def runKeysMacro(profileNum):

    def RUN(replaced, replacement):
        keyboard = Controller()

        pressed = False

        print("\n\n\nHit escape to exit!\n\nStarting vMacro (Keyboard).\n")

        def on_press(key):
            global pressed
            pressed = True
            if pressed == False:
                print(f"{key} pressed.")
            else:
                print(f"{key} held down.")

        def pressKey():
            # keyboard.press(replacement)
            # time.sleep(0.05)
            # keyboard.release(replacement)
            replacementStr = str(replacement).replace("Key.", "")
            pyautogui.press(replacementStr)

        def on_release(key):

            global pressed
            pressed = False
            if str(key) == "Key.esc":
                print("\nExited vMacro.\n")
                os.startfile("../vMacro/logs/keysPressed.txt")
                sys.exit()
                return False  # break out of loop
            elif str(key).replace("'", "") == replaced:
                pressKey()
            elif str(key) == str(replaced):
                pressKey()
            else:
                print(f"{key} released.")

        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()  # loop until broken out

    profileNum = int(str(profileNum)[-1:])
    # getData
    thisFolder = os.path.dirname(os.path.abspath(
        __file__)) + f"/profiles/profile{profileNum}/"
    my_file = os.path.join(thisFolder, "macro.txt")
    f = open(my_file, "r")
    profileInfo = f.readlines()
    f.close()
    # pName = (profileInfo[0]).replace("\n", "")
    pReplaced = (profileInfo[1]).replace("\n", "")
    pReplacement = (profileInfo[2]).replace("\n", "")

    RUN(pReplaced, pReplacement)
