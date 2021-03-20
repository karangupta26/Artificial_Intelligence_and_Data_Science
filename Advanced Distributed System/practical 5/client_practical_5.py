import time 
import sysv_ipc
import sys
MQ_KEY=1024
mqueue = None

while not mqueue:
    try:
        mqueue = sysv_ipc.MessageQueue(MQ_KEY, sysv_ipc.IPC_CREX, max_message_size=4096)
    except sysv_ipc.ExistentialError:
        print('Queue is not initialize, wait...')
        mqueue = sysv_ipc.MessageQueue(MQ_KEY)
        time.sleep(1)

while True:
    try:
        msg=str(input("Enter a message from client : "))
        mqueue.send(msg.encode())
        time.sleep(10)
        message, ntype = mqueue.receive()
        if message.decode().upper()=='STOP' or message.decode().upper()=='KEYBOARDINTERRUPT':
            print("Existing the system.")
            mqueue.remove()
            sys.exit()
    
        print('client recieved this message: ', message.decode())
    except KeyboardInterrupt:
        mqueue.send('KeyboardInterrupt'.encode())
        mqueue.remove()
        sys.exit()
    except sysv_ipc.ExistentialError:
        print("Existing the system.")
        sys.exit()