import time 
import sysv_ipc
import sys
import os

SHM_KEY = 1024
SHM_SIZE = 128
shared_memory=None

while not shared_memory:
		try:
			shared_memory = sysv_ipc.SharedMemory(SHM_KEY, size=SHM_SIZE)
		except sysv_ipc.ExistentialError:
			print('Shared Memory is not initialize, wait...')
			time.sleep(1)
while True:
    try:
        time.sleep(5)
        message = shared_memory.read().decode().split()
        finalmessage=message[1][:int(message[0])]
        
        if str(finalmessage).upper()=='STOP' or str(finalmessage).upper()=='KEYBOARDINTERRUPT':
            print("Existing the system.")
            shared_memory.remove()
            sys.exit()
        print('Server recieved this message: ', finalmessage)
        msg=str(input("Enter a message from server : "))
        finalmsg=str(len(msg))+" "+msg
        shared_memory.write(finalmsg.encode())
    except KeyboardInterrupt:
        msg=str(len('KeyboardInterrupt'))+" "+'KeyboardInterrupt'
        shared_memory.write(msg.encode())
        shared_memory.remove()
        sys.exit()
    except sysv_ipc.ExistentialError:
        print("Existing the system.")
        sys.exit()