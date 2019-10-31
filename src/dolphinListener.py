import sh
import sys
import os
import re
import time

class listener():

    @staticmethod
    def get_pid():
        ps = sh.grep(sh.ps("a"), "dolphin-emu")
        pid = re.findall("\d+", str(ps))[0]
        return pid, ps 

    
    def __init__(self): #do we need any params passed
        pass
        self.pid , self.ps = listener.get_pid()
        # open the maps and mem files of the process
        print(self.ps)
        self.maps = "/proc/{}/maps".format(self.pid)
        print("[*] maps: {}".format(self.maps))
        self.mem = "/proc/{}/mem".format(self.pid)
        print("[*] mem: {}".format(self.maps))
        self.parser_maps()

    def next(self, addy):
        pass

    def parser_maps(self):
        try:
            maps_file = open('/proc/{}/maps'.format(self.pid), 'r')
        except IOError as e:
            print("[ERROR] Can not open file {}:".format(self.maps))
            print("        I/O error({}): {}".format(e.errno, e.strerror))
            sys.exit(1)

        afterHeap= False
        for line in maps_file:
            sline = line.split(' ')



            # check if we found the heap
            if sline[-1][:-1] != "[heap]" and not afterHeap:
                continue
            print("[*] Found [heap]:")

            if afterHeap:
                self.vmem_start = sline[0].split("-")[0]
                print("[*] Found virtual memory start adress: {}".format(self.vmem_start))
                afterHeap= False
                break

            afterHeap = True

            # parse line
            addr = sline[0]
            perm = sline[1]
            offset = sline[2]
            device = sline[3]
            inode = sline[4]
            pathname = sline[-1][:-1]
            print("\tpathname = {}".format(pathname))
            print("\taddresses = {}".format(addr))
            print("\tpermisions = {}".format(perm))
            print("\toffset = {}".format(offset))
            print("\tinode = {}".format(inode))

            # check if there is read and write permission
            if perm[0] != 'r' or perm[1] != 'w':
                print("[*] {} does not have read/write permission".format(pathname))
                maps_file.close()
                exit(0)

            # get start and end of the heap in the virtual memory
            addr = addr.split("-")
            if len(addr) != 2: # never trust anyone, not even your OS :)
                print("[*] Wrong addr format")
                maps_file.close()
                exit(1)
            addr_start = int(addr[0], 16)
            addr_end = int(addr[1], 16)
            print("\tAddr start [{:x}] | end [{:x}]".format(addr_start, addr_end))

            # # open and read mem
            # try:
            #     mem_file = open(mem_filename, 'rb+')
            # except IOError as e:
            #     print("[ERROR] Can not open file {}:".format(mem_filename))
            #     print("        I/O error({}): {}".format(e.errno, e.strerror))
            #     maps_file.close()
            #     exit(1)

    def test(self):
        with open(self.mem, 'rb+') as mem_file:
            mem_file.seek(int(self.vmem_start,16))#+ int('0CAC434', 16))
            val = int.from_bytes(mem_file.read(1), 'big')
            print(val)
            time.sleep(1)


l = listener()
print(l.pid)
i =0
# while(True):
#     l.test()
#     print(i)
#     i+=1
#     #time.sleep(0.01)