# Practical 3 - Perform inter-process communication between a Parent and Child process
# This two-communication must continue till a specific key is pressed or 
# a STOP message is sent by any one of the processes.
########################################################
# Author    -   Karan Gupta
# Roll No.  -   2020PMD4224
# Degree    -   M.Tech (Mobile Computing and Data Analytics)
#########################################################
import os, time, sys
mypid = os.getpid()
parentpid = os.getppid()
sys.stderr.write('Child %d of %d got arg: "%s"\n' %(mypid, parentpid, sys.argv[1]))
i=0
while True:
    try:
        time.sleep(3)                                                   # make parent process wait by sleeping here
        recv = input()                                                  # stdin tied to pipe: comes from parent's stdout
        time.sleep(3)
        if recv=="Stop" or recv=="End":
            sys.exit(0)
        if i == 30:                                                     # value at which you have to send End Message From child
            send="End"
            print(send)                                                 # stdout tied to pipe: goes to parent's stdin
            sys.stdout.flush()                                          # make sure it's sent now or else process blocks
            sys.exit()
        else:
            send = 'Child %d got: [%s]' % (mypid, recv)
        print(send)                                                     # stdout tied to pipe: goes to parent's stdin
        sys.stdout.flush()                                              # make sure it's sent now or else process blocks
        i+=1    
    except KeyboardInterrupt:                                           # Keyboard Interrupt
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)