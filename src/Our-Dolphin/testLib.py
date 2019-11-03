#!/usr/bin/python
import sys
sys.path.insert(0, "Source/build")
from DolphinMemoryEngine import MemoryWatcher

d = MemoryWatcher(0x80CAC434, 'w')
status = d.hook()
print(status)
oldmem = ""
while(d.getStatus() == 'hooked'):
    mem = d.getMemory()
    if (mem!=oldmem):
        oldmem = mem
        print(mem)