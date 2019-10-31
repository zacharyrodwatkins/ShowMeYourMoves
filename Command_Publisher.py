import os
import time
import numpy as np

path = "> ~/.local/share/dolphin-emu/Pipes/pipe1"
FRAME_LEN = 1.0/60.0  # 60 fps
WD_PAUSE = .05  # Time to wait after jumping before airdodging into WD
WD_DURATION = 0.15  # Time to wait after WD before next input
SHFF_PAUSE = 0.3  # Time to wait after SH before FF
LC_PAUSE = 0.010  # Time to wait after FF before LC
UP, DOWN = ('1', '0')
RIGHT, LEFT = ('1', '0')
CENTER = '0.5'


def Press_Button(Button):
    os.system('echo' + ' ' + 'PRESS ' + Button + ' ' + path)
    time.sleep(FRAME_LEN)
    os.system('echo' + ' ' + 'RELEASE ' + Button + ' ' + path)
    time.sleep(FRAME_LEN)


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


def Wavedash(Direction):
    Press_Button('X')
    Move_Stick(Direction, DOWN)
    time.sleep(WD_PAUSE)
    Press_Button('L')
    Move_Stick(CENTER, CENTER)
    time.sleep(WD_DURATION)


def Hold_Button(Button, time):
    os.system('echo' + ' ' + 'PRESS ' + Button + ' ' + path)
    time.sleep(time)
    os.system('echo' + ' ' + 'RELEASE ' + Button + ' ' + path)


def dash(direction):
    if direction == RIGHT:
        Move_Stick(RIGHT, CENTER)
    if direction == LEFT:
        Move_Stick(LEFT, CENTER)


def fastfall():
    Move_Stick(CENTER, DOWN)
    time.sleep(FRAME_LEN)
    Move_Stick(CENTER, CENTER)


def FF_L_cancel():
    time.sleep(SHFF_PAUSE - FRAME_LEN)
    fastfall()
    time.sleep(LC_PAUSE)
    Press_Button("L")


def SHFFLED_arial(Direction):
    if Direction == 'NEUTRAL':
        Press_Button('X')
        time.sleep(2*FRAME_LEN)
        Press_Button('A')
        FF_L_cancel()

    if Direction == 'UP':
        Press_Button('X')
        time.sleep(2*FRAME_LEN)
        Move_Stick(CENTER, UP)
        Press_Button('A')
        Move_Stick(CENTER, CENTER)
        FF_L_cancel()

    if Direction == 'DOWN':
        Press_Button('X')
        time.sleep(2*FRAME_LEN)
        Move_Stick(CENTER, DOWN)
        Press_Button('A')
        Move_Stick(CENTER, CENTER)
        FF_L_cancel()

    if Direction == 'LEFT':
        Press_Button('X')
        time.sleep(2*FRAME_LEN)
        Move_Stick(LEFT, CENTER)
        Press_Button('A')
        Move_Stick(CENTER, CENTER)
        FF_L_cancel()

    if Direction == 'RIGHT':
        Press_Button('X')
        time.sleep(2*FRAME_LEN)
        Move_Stick(RIGHT, CENTER)
        Press_Button('A')
        Move_Stick(CENTER, CENTER)
        FF_L_cancel()


def Smash_Attack(Direction, Charge):
    if Direction == 'UP':
        Move_Stick('0.5', '0')
        Hold_Button('A', Charge)
        Move_Stick('0.5', '0.5')

    if Direction == 'DOWN':
        Move_Stick('0.5', '1')
        Hold_Button('A', Charge)
        Move_Stick('0.5', '0.5')

    if Direction == 'LEFT':
        Move_Stick('0', '0.5')
        Hold_Button('A', Charge)
        Move_Stick('0.5', '0.5')

    if Direction == 'RIGHT':
        Move_Stick('1', '0.5')
        Hold_Button('A', Charge)
        Move_Stick('0.5', '0.5')


def Special_Move(Direction):
    if Direction == 'DOWN':
        Move_Stick('0.5', '1')
        Press_Button('B')
        Move_Stick('0.5', '0.5')

    if Direction == 'LEFT':
        Move_Stick('0', '0.5')
        Press_Button('B')
        Move_Stick('0.5', '0.5')

    if Direction == 'RIGHT':
        Move_Stick('1', '0.5')
        Press_Button('B')
        Move_Stick('0.5', '0.5')


while True:
    SHFFLED_arial("NEUTRAL")
    time.sleep(10*FRAME_LEN)
    SHFFLED_arial("UP")
    time.sleep(10*FRAME_LEN)
    SHFFLED_arial("DOWN")
    time.sleep(10*FRAME_LEN)
    SHFFLED_arial("LEFT")
    time.sleep(10*FRAME_LEN)
    SHFFLED_arial("RIGHT")
    time.sleep(10*FRAME_LEN)
