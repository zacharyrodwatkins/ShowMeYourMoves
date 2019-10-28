import os
import time
path = "> ~/.local/share/dolphin-emu/Pipes/pipe1"


def Press_Button(Button):
    os.system('echo' + ' ' + 'PRESS ' + Button + ' ' + path)
    time.sleep(0.001)
    os.system('echo' + ' ' + 'RELEASE ' + Button + ' ' + path)


def Move_Stick(X, Y):
    os.system('echo' + ' ' + 'SET MAIN ' + X + ' ' + Y + ' ' + path)


def Calibrate_MAIN_STICK():
    x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    y = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    for X in x:
        for Y in y:
            Move_Stick(str(X), str(Y))
            time.sleep(1)


# Calibrate_MAIN_STICK()
def Show_Your_Moves():
    i = 0
    for i in range(6000):
        Press_Button('D_UP')


# Show_Your_Moves()
