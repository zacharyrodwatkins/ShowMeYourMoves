import os
import time
path = "> ~/.local/share/dolphin-emu/Pipes/pipe1"
Button_Pause = 1.0/60.0
After_jump_Pause = 0.05


def Press_Button(Button):
    os.system('echo' + ' ' + 'PRESS ' + Button + ' ' + path)
    time.sleep(Button_Pause)
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


def Wavedash(Direction):
    if Direction == "LEFT":
        Press_Button('X')
        time.sleep(After_jump_Pause)
        Move_Stick('0', '1')
        Hold_Button('L', Button_Pause)
        Move_Stick('0.5', '0.5')

    if Direction == "RIGHT":
        Press_Button('X')
        time.sleep(After_jump_Pause)
        Move_Stick('1', '1')
        Hold_Button('L', Button_Pause)
        Move_Stick('0.5', '0.5')


def Hold_Button(Button, TIME):
    os.system('echo' + ' ' + 'PRESS ' + Button + ' ' + path)
    time.sleep(TIME)
    os.system('echo' + ' ' + 'RELEASE ' + Button + ' ' + path)


Wavedash('LEFT')
time.sleep(0.15)
Wavedash('RIGHT')
time.sleep(0.3)


def Short_Hop_Attack(Direction):
    if Direction == 'NEUTRAL':
        Press_Button('X')
        time.sleep(After_jump_Pause)
        Press_Button('A')

    if Direction == 'UP':
        Press_Button('X')
        time.sleep(After_jump_Pause)
        Move_Stick('0.5', '0')
        Press_Button('A')
        Move_Stick('0.5', '0.5')

    if Direction == 'DOWN':
        Press_Button('X')
        time.sleep(After_jump_Pause)
        Move_Stick('0.5', '1')
        Press_Button('A')
        Move_Stick('0.5', '0.5')

    if Direction == 'LEFT':
        Press_Button('X')
        time.sleep(After_jump_Pause)
        Move_Stick('0', '0.5')
        Press_Button('A')
        Move_Stick('0.5', '0.5')

    if Direction == 'RIGHT':
        Press_Button('X')
        time.sleep(After_jump_Pause)
        Move_Stick('1', '0.5')
        Press_Button('A')
        Move_Stick('0.5', '0.5')


Short_Hop_Attack('DOWN')
time.sleep(1)
Short_Hop_Attack('RIGHT')
time.sleep(1)


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


Smash_Attack('RIGHT', 0.5)
time.sleep(1)


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


Special_Move('LEFT')
time.sleep(1)
