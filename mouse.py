import os
from pynput.keyboard import Key, Listener, Controller
from pynput.mouse import Button, Controller, Listener
from pynput import mouse
import time
from PIL import ImageTk, Image

mouse = Controller()

mouseMonitorList = []

recordingMouse = True
replayRunning = True

replayTimeCounter = 0

timeInterval = 0.05
maxTime = 3


def clearRunningScripts():
    try:
        if os.path.exists("../vMacro/logs/keysRunning.txt"):
            os.remove("../vMacro/logs/keysRunning.txt")
        if os.path.exists("../vMacro/logs/mouseRunning.txt"):
            os.remove("../vMacro/logs/mouseRunning.txt")
    except:
        pass


def replayMouse():
    print("\nReplay")
    global replayTimeCounter
    global timeInterval
    global maxTime
    for mousePos in mouseMonitorList:
        if replayTimeCounter <= maxTime:
            # Move = tuple(map(lambda x, y: x - y, mouse.position, mousePos))
            # print(Move)
            # mouse.move = Move
            mouse.position = mousePos
            # replayTimeCounter = round(replayTimeCounter + timeInterval, 1)
            replayTimeCounter = round(
                replayTimeCounter, 1) + round(timeInterval, 1)
            time.sleep(timeInterval)
            # print("mouse move")
            if replayTimeCounter > maxTime:
                # if replayTimeCounter == maxTime - timeInterval:
                print("Mouse click.")
                mouse.click(Button.left, 2)
                clearRunningScripts()


def mouseRecord(timeInterv, time):
    global mouseMonitorList
    global recordingMouse
    global replayTimeCounter
    global timeInterval
    global maxTime
    replayTimeCounter = 0
    # global startTime
    timeCounter = 0
    while recordingMouse:
        if timeCounter < maxTime:
            timeCounter += timeInterval
            print(mouse.position)
            mouseMonitorList.append(mouse.position)
            time.sleep(timeInterval)
        else:
            writeMouse()
            # replayMouse()
            recordingMouse = False


def writeMouse():
    f = open("../vMacro/logs/mouseMonitor.txt", "w")
    f.write(str(mouseMonitorList))
    f.close()


def startMouseRecord(timeInterv, time):
    clearRunningScripts()
    print("\n\n\nHit escape to exit!\n\nStarting vMacro (Mouse).\n")

    f = open("../vMacro/logs/mouseRunning.txt", "w")
    f.write("Running")
    f.close()

    mouseRecord(timeInterv, time)


# def on_click(x, y, button, pressed):
#     print("test")
#     global mouseScriptRunning
#     if pressed:
#         print("test")
#         if button == Button.right:
#             mouseScriptRunning = False
#             replay()
# writeMouse()
# elif key == Key.esc:
#     mouseScriptRunning = False
#     replay()
#     writeMouse()


# def on_scroll(x, y, dx, dy):
#     pass


# with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
#     listener.join()


# mouse = Controller()

# mouseMonitorList = []

# mouseScriptRunning = True

# # startTime = time.time()


# def mouseRecord():
#     global mouseMonitorList
#     global mouseScriptRunning
#     # global startTime
#     while mouseScriptRunning:
#         print(mouse.position)
#         time.sleep(0.2)
#         mouseMonitorList.append(mouse.position)


# def writeMouse():
#     f = open("mouseMonitor.txt", "w")
#     f.write(str(mouseMonitorList))
#     f.close()
#     # os.startfile("mouseMonitor.txt")


# # def on_press(key):
# #     global mouseScriptRunning
# #     if key == Key.enter:
# #         mouseScriptRunning = False
# #         replay()
# #         writeMouse()
# #     elif key == Key.esc:
# #         mouseScriptRunning = False
# #         replay()
# #         writeMouse()


# def replay():
#     print("\nREPLAY")
#     for mousePos in mouseMonitorList:
#         mouse.position = mousePos
#         time.sleep(0.2)


# # def on_release():
# #     pass


# def on_move(x, y):
#     pass


# def on_click(x, y, button, pressed):
#     global mouseScriptRunning
#     if button == Button.right:
#         mouseScriptRunning = False
#         replay()
#         # writeMouse()
#     # elif key == Key.esc:
#     #     mouseScriptRunning = False
#     #     replay()
#     #     writeMouse()


# def on_scroll(x, y, dx, dy):
#     pass


# mouseRecord()

# with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mouseListener:
#     mouseListener.join()
# # with Listener(on_press=on_press, on_release=on_release) as listener:
# #     listener.join()  # loop until broken out
