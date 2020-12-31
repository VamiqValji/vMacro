import sys
from pynput.keyboard import Key, Listener, Controller
import pynput
import os
import time
from os import listdir
from os.path import isfile, join
# import pyautogui


def runKeysMacro(profileNum):

    def RUN(replaced, replacement):
        keyboard = Controller()

        pressed = False

        def clearRunningScripts():
            try:
                # if os.path.exists("../vMacro/logs/keysMacroRunning.txt"):
                #     f = open("../vMacro/logs/keysMacroPressed.txt", "r")
                #     fp = open(
                #         "../vMacro/logs/keysMacroPressed_prev_log.txt", "w")
                #     fp.write(f.read())
                #     f.close()
                #     fp.close()
                #     os.remove("../vMacro/logs/keysMacroRunning.txt")
                # if os.path.exists("mouseMacroRunning.txt"):
                #     os.remove("../vMacro/logs/mouseMacroRunning.txt")
                pass
            except:
                pass

        clearRunningScripts()
        print("\n\n\nHit escape to exit!\n\nStarting vMacro (Keyboard).\n")

        # f = open("../vMacro/logs/keysMacroRunning.txt", "w")
        # f.write("Running")
        # f.close()

        def on_press(key):
            global pressed
            pressed = True
            if pressed == False:
                print(f"{key} pressed.")
            else:
                print(f"{key} held down.")

        def on_release(key):

            global pressed
            pressed = False
            # print(key == f"'{replaced}'")
            # print(f"'{replaced}'")
            if key == Key.esc:
                print("\nExited vMacro.\n")
                os.startfile("../vMacro/logs/keysPressed.txt")
                clearRunningScripts()
                return False  # break out of loop
            elif key == Key.enter:
                print("done")
                clearRunningScripts()
                sys.exit()
                return False
            elif str(key).replace("'", "") == replaced:
                keyboard.press(replacement)
                time.sleep(0.05)
                keyboard.release(replacement)
                # pyautogui.press(replacement)
                pass
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
