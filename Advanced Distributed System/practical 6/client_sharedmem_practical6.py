import time 
import sysv_ipc
import sys
import os

SHM_KEY = 1024
SHM_SIZE = 128
shared_memory = None

while not shared_memory:
    try:
        shared_memory = sysv_ipc.SharedMemory(SHM_KEY, sysv_ipc.IPC_CREX, size=SHM_SIZE)
    except sysv_ipc.ExistentialError:
        print('Queue is not initialize, wait...')
        shared_memory = sysv_ipc.SharedMemory(SHM_KEY, size=SHM_SIZE)
        time.sleep(1)

while True:
    try:
        msg=str(input("Enter a message from client : "))
        finalmsg= str(len(msg))+" "+msg
        shared_memory.write(finalmsg.encode())
        time.sleep(10)
        message = shared_memory.read().decode().split()
        finalmessage=message[1][:int(message[0])]
        if str(finalmessage).upper()=='STOP' or str(finalmessage).upper()=='KEYBOARDINTERRUPT':
            print("Existing the system.")
            shared_memory.remove()
            sys.exit()
    
        print('client recieved this message: ', finalmessage)
    except KeyboardInterrupt:
        msg=str(len('KeyboardInterrupt'))+" "+'KeyboardInterrupt'
        shared_memory.write(msg.encode())
        shared_memory.remove()
        sys.exit()
    except sysv_ipc.ExistentialError:
        print("Existing the system.")
        sys.exit()