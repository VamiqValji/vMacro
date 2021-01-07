import time
import os
from os import listdir
from os.path import isfile, join
import pynput
from pynput.keyboard import Key, Listener
import sys


def record(profNum, RorR):
    print(
        "\n\n\nRECORD KEY INPUT BY PRESSING ANY BUTTON ON THE KEYBOARD\n")

    def on_press(key):

        if key != Key.esc:

            print(key)

            # os.remove(
            #     f"../vMacro/profiles/{profNum}/replaced_OR_replacement.txt")

            if RorR == "replaced":
                my_file = os.path.join(profFolder, "recordingReplaced.txt")
                f = open(my_file, "w")
                f.write(str(key).strip("'"))
                f.close()
            elif RorR == "replacement":
                my_file = os.path.join(profFolder, "recordingReplacement.txt")
                f = open(my_file, "w")
                f.write(str(key).strip("'"))
                f.close()

            print(f"{key} pressed.")

            # os.remove(
            #     f"../vMacro/profiles/{profNum}/recordingReplaced.txt")
            # os.remove(
            #     f"../vMacro/profiles/{profNum}/recordingReplacement.txt")

            sys.exit()
        else:
            print("Please choose a key other than escape.")

    with Listener(on_press=on_press) as listener:
        listener.join()  # loop until broken out


def getInfo():

    global profFolder

    profFolder = os.path.dirname(os.path.abspath(
        __file__)) + "/profiles/"  # + f"/logs/"

    # my_file = os.path.join(profFolder, "profNum.txt")
    my_file = f"../vMacro/profiles/profNum.txt"
    f = open(my_file, "r")
    profNum = f.read()
    f.close()

    # os.remove(my_file)

    profFolder = profFolder + f"{profNum}/"

    my_file = os.path.join(profFolder, "recordingInputInfo.txt")
    f = open(my_file, "r")
    recInfo = f.readlines()
    f.close()

    RorR = recInfo[0]
    # profNum = recInfo[0]

    record(profNum, RorR)


getInfo()

# with Listener(on_press=on_press) as listener:
#     listener.join()  # loop until broken out
