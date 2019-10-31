import time
import subprocess
import signal
import ptrace.debugger
import sys


def debugger_example(pid):
    debugger = ptrace.debugger.PtraceDebugger()

    print("Attach the running process %s" % pid)
    process = debugger.addProcess(pid, False)
    # process is a PtraceProcess instance
    print("IP before: %#x" % process.getInstrPointer())

    print("Execute a single step")
    process.singleStep()
    # singleStep() gives back control to the process. We have to wait
    # until the process is trapped again to retrieve the control on the
    # process.
    process.waitSignals(signal.SIGTRAP)
    print("IP after: %#x" % process.getInstrPointer())

    process.detach()
    debugger.quit()


def print_memory_of_pid(pid, only_writable=True):
    """ 
    Run as root, take an integer PID and return the contents of memory to STDOUT
    """
    memory_permissions = 'rw' if only_writable else 'r-'
    sys.stderr.write("PID = %d" % pid)
    with open("/proc/%d/maps" % pid, 'r') as maps_file:
        with open("/proc/%d/mem" % pid, 'r', 0) as mem_file:
            for line in maps_file.readlines():  # for each mapped region
                m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r][-w])', line)
                if m.group(3) == memory_permissions: 
                    sys.stderr.write("\nOK : \n" + line+"\n")
                    start = int(m.group(1), 16)
                    if start > 0xFFFFFFFFFFFF:
                        continue
                    end = int(m.group(2), 16)
                    sys.stderr.write( "start = " + str(start) + "\n")
                    mem_file.seek(start)  # seek to region start
                    chunk = mem_file.read(end - start)  # read region contents
                    print chunk,  # dump contents to standard output
                else:
                    sys.stderr.write("\nPASS : \n" + line+"\n")


def get_pid(name):
    return subprocess.check_output(["pidof",name])


if __name__ == '__main__': # Execute this code when run from the commandline.
    try:
        pid = int(get_pid("dolphin-emu"))
        debugger_example(pid)
    except (AssertionError, ValueError) as e:
        print(e)
