import os
import time
path = "> ~/.local/share/dolphin-emu/Pipes/pipe1"
Button_Pause = 1.0/60.0


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
        time.sleep(0.05)
        Move_Stick('0', '1')
        Hold_Button('L', Button_Pause)
        Move_Stick('0.5', '0.5')

    if Direction == "RIGHT":
        Press_Button('X')
        time.sleep(0.05)
        Move_Stick('1', '1')
        Hold_Button('L', Button_Pause)
        Move_Stick('0.5', '0.5')


def Hold_Button(Button, TIME):
    os.system('echo' + ' ' + 'PRESS ' + Button + ' ' + path)
    time.sleep(TIME)
    os.system('echo' + ' ' + 'RELEASE ' + Button + ' ' + path)


# Wavedash('LEFT')
# time.sleep(0.15)
# Wavedash('RIGHT')

def Short_Hop_Attack(Attack):
    if Attack == 'NEUTRAL':

    
    if Attack == 'UP':

    
    if Attack == 'STOMP':

    
    if Attack == 'KNEE':
        Press_Button('X')
        time.sleep(Button_Press)
    
    if Attack == 'BACK_SLAP':


    