import time
import os
from os import listdir
from os.path import isfile, join
import pynput
from pynput.keyboard import Key, Listener
import sys


def record(profileLoc, RorR):
    print(
        "\n\n\nRECORD YOUR KEY BY PRESSING ANY BUTTON ON THE KEYBOARD\n")

    def on_press(key):

        if key != Key.esc:

            print(key)

            os.remove(
                f"../vMacro/profiles/{profileLoc}/replaced_OR_replacement.txt")

            if RorR == "replaced":
                my_file = os.path.join(profFolder, "recordingReplaced.txt")
                f = open(my_file, "w")
                f.write(key)
                f.close()
            elif RorR == "replacement":
                my_file = os.path.join(profFolder, "recordingReplacement.txt")
                f = open(my_file, "w")
                f.write(key)
                f.close()

            print(f"{key} pressed.")

            # os.remove(
            #     f"../vMacro/profiles/{profileLoc}/recordingReplaced.txt")
            # os.remove(
            #     f"../vMacro/profiles/{profileLoc}/recordingReplacement.txt")

            sys.exit()
        else:
            print("Please choose a key other than escape.")

    with Listener(on_press=on_press) as listener:
        listener.join()  # loop until broken out


def getInfo(profileLoc):

    global profFolder
    profFolder = os.path.dirname(os.path.abspath(
        __file__)) + f"/profiles/{profileLoc}/"  # + f"/logs/"

    my_file = os.path.join(profFolder, "replaced_OR_replacement.txt")
    f = open(my_file, "r")
    replacedOrReplacement = f.readlines()
    f.close()

    RorR = replacedOrReplacement[0]

    record(profileLoc, RorR)

# with Listener(on_press=on_press) as listener:
#     listener.join()  # loop until broken out
