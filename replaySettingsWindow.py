from tkinter import *
from tkinter import messagebox
import os
from os import listdir
from os.path import isfile, join
import asyncio
import time
from defaultSettings import importDefaultSettings
from defaultSettings import getColor


def getFilePath(dir, file):
    thisFolder = os.path.dirname(os.path.abspath(
        __file__)) + dir
    return os.path.join(thisFolder, file)


def openReplaySettingsWindow(keysPressedScript):

    def update():
        update = Tk()
        # bgColor = getColor("bg")
        # textColor = getColor("text")
        importDefaultSettings(update)

        messagebox.showinfo(
            "Changes Saved", "The replay keyboard script was overwrited. If your script doesn't work in replay mode, please either try again at making your own script or just use the record feature.")

        update.mainloop()

    def saveChanges():
        textInput = scriptEditorInput.get("1.0", 'end-1c')
        f = open(getFilePath("/logs/", "keysPressed.txt"), "w")
        f.write(textInput)
        f.close()
        update()

    def text(t, yPadding):
        t = str(t)
        yPadding = int(yPadding)
        return Label(
            root, text=t, pady=yPadding, bg=bgColor, fg=textColor).pack()

    root = Tk()
    bgColor = getColor("bg")
    textColor = getColor("text")
    importDefaultSettings(root)

    Label(
        root, text="Keyboard Script", pady="10", bd=4, bg=bgColor, fg=textColor).pack()

    Label(
        root, text="", pady="5", bd=4, bg=bgColor, fg=textColor).pack()

    text("Creating a keyboard script is more simple than you think! Write the character you want to be pressed,", 0)
    text("then write the duration you want it to be pressed down for (in seconds). Every letter MUST be", 0)
    text("followed by a duration in seconds, and the script can NEVER start with a duration.", 0)
    text("The 'wait' keyword signifies no button presses for the duration followed by it.", 0)
    text("", 3)
    text("For example, the output of 'wait,2,b,0.1,o,0.1,b,0.1' would be:", 0)
    text("Wait for 2 seconds, then tap the 'b' key for 0.1 seconds,", 0)
    text("then tap the 'o' key for 0.1 seconds. And finally, tap", 0)
    text("the 'b' key again for 0.1 seconds; outputting 'bob'.", 0)

    text("", 6)
    text("If your script doesn't work in replay mode, please either try again", 0)
    text("at making your own script or just use the record feature.", 0)

    Label(
        root, text="", pady="5", bd=4, bg=bgColor, fg=textColor).pack()

    global scriptEditorInput
    scriptEditorInput = Text(
        root, width=100, height=10, bg=bgColor, fg=textColor)
    scriptEditorInput.insert(INSERT, keysPressedScript)
    scriptEditorInput.pack()

    # text("Output:", 6)
    text("", 3)
    Button(root, text="Save Changes", pady=5,
           padx=5, command=saveChanges, bg=bgColor, fg=textColor).pack()
    global changesSavedLabel
    changesSavedLabel = Label(root, text="", pady=1, bg=bgColor, fg=textColor)
    text("", 4)
    # Button(root, text="View Output", pady=5, padx=5, command=output).pack()
    # text("", 2)
    # outputLabel = Label(
    #     root, text="Output:{ }", pady=2)
    # outputLabel.pack()

    mainloop()


def getInfo():

    f = open(getFilePath("/logs/", "keysPressed.txt"), "r")
    keysPressedScript = f.read()
    f.close()

    openReplaySettingsWindow(keysPressedScript)


getInfo()
