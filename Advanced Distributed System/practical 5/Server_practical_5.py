import time 
import sysv_ipc
import sys

MQ_KEY=1024
mqueue = None

while not mqueue:
		try:
			mqueue = sysv_ipc.MessageQueue(MQ_KEY)
		except sysv_ipc.ExistentialError:
			print('Queue is not initialize, wait...')
			time.sleep(1)
while True:
    try:
        time.sleep(5)
        message, ntype = mqueue.receive()
        if message.decode().upper()=='STOP' or message.decode().upper()=='KEYBOARDINTERRUPT':
            print("Existing the system.")
            mqueue.remove()
            sys.exit()
        print('Server recieved this message: ', message.decode())
        msg=str(input("Enter a message from server : "))
        mqueue.send(msg.encode())
    except KeyboardInterrupt:
        mqueue.send('KeyboardInterrupt'.encode())
        mqueue.remove()
        sys.exit()
    except sysv_ipc.ExistentialError:
        print("Existing the system.")
        sys.exit()