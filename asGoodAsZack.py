#!/usr/bin/python
from Command_Publisher import *
import sys
sys.path.insert(0, 'src/Our-Dolphin/Source/build')
from DolphinMemoryEngine import MemoryWatcher

p1x_add = 0x804510D0
p2x_add = 0x80451F60


p1=MemoryWatcher(p1x_add,'f')
p2=MemoryWatcher(p2x_add, 'f')

while(p1.getStatus()=='hooked'):

    p1x = float(p1.getMemory())
    p2x = float(p2.getMemory())

    if abs(p1x-p2x)<10:
        Move_Stick('0.5','0.5')
        Press_Button('B')
        #print("Falco Punch!")

    else:
        x_stick = 1 if p2x<p1x else 0
        x_stick = str(x_stick)
        print(x_stick)
        Move_Stick(x_stick, str(0.5))