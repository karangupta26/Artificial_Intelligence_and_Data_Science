# Practical 3 - Perform inter-process communication between two child processes
# This two-communication must continue till a specific key is pressed or 
# a STOP message is sent by any one of the processes.
########################################################
# Author    -   Karan Gupta
# Roll No.  -   2020PMD4224
# Degree    -   M.Tech (Mobile Computing and Data Analytics)
#########################################################
import os, sys, signal
def spawn(prog, *args):                                                                 # pass progname, cmdline args

    stdinFd = sys.stdin.fileno()                                                        # get descriptors for streams
    stdoutFd = sys.stdout.fileno()                                                      # normally stdin=0, stdout=1
    child1Stdin, child2Stdout = os.pipe()                                               # make two IPC pipe channels
    child2Stdin, child1Stdout = os.pipe()                                               # pipe returns (inputfd, outoutfd)

    pid1 = os.fork()                                                                    # make two copies of this process
    pid2 = os.fork()
    if pid1>0 and pid2>0:
        print("I am Parent Process and My child will Communicate and my process Id is : ",os.getpid())
        print("Child 1 Process Id : ",pid1)
        print("Child 2 Process Id : ",pid2)
        
    elif pid1==0 and pid2>0:
        os.close(child2Stdout)                                                           # in first child process after fork:
        os.close(child2Stdin)                                                            # close child2 ends in child 1
        os.dup2(child1Stdin, stdinFd)                                                    # my sys.stdin copy = pipe1[0]
        os.dup2(child1Stdout, stdoutFd)                                                  # my sys.stdout copy = pipe2[1]
        mypid=os.getpid()
        print('Hello 1 from Child 1 (', mypid,')',sep='')                                # to child 1's stdin
        sys.stdout.flush()                                                               # subvert stdio buffering
        reply = input()                                                                  # from child 1's stdout
        sys.stderr.write('Child 1 got: "%s"\n' % reply)                                  # stderr not tied to pipe!
        i=2
        while True:
            try:
                if i==45:                                                                # value at which you have to send End Message From Parent
                    print("End")
                    sys.stderr.write("Child 1 has sent 'End' Message\n")
                    sys.exit(0)
                else:
                    print('Hello ',i,' from Child 1 (',mypid,')',sep='')

                sys.stdout.flush()                                                       # subvert stdio buffering
                reply = sys.stdin.readline()                                             # read the Latest Reply from the pipe
                if reply[:-1]=="Stop" or reply[:-1]=="End":
                    sys.stderr.write('Child 1 got: "%s"\n' % reply[:-1])
                    sys.exit()
                else:
                    sys.stderr.write('Child 1 got: "%s"\n' % reply[:-1])
                i+=1
            except KeyboardInterrupt:                                                    # Keyborad interrupt
                print('Interrupted')
                try:
                    sys.exit(0)
                except SystemExit:
                    os._exit(0)

    elif pid2==0 and pid1>0:
        os.close(child1Stdin)                                                           # in child 2 process after fork:
        os.close(child1Stdout)                                                          # close child 1's ends in child
        os.dup2(child2Stdin, stdinFd)                                                   # my sys.stdin copy = pipe2[0]
        os.dup2(child2Stdout, stdoutFd)                                                 # my sys.stdout copy = pipe1[1]
        args = (prog,) + args
        os.execvp(prog, args)                                                           # new program in this process
        assert False, 'execvp failed!'                                                  # os.exec call never returns here

if __name__ == '__main__':
    #mypid = os.getpid()
    spawn('python3', 'pipetest-2.py', 'spam')                                           # fork child processes
    