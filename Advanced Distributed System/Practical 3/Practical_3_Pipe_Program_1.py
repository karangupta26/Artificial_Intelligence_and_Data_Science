# Practical 3 - Perform inter-process communication between a Parent and Child process
# This two-communication must continue till a specific key is pressed or 
# a STOP message is sent by any one of the processes.
########################################################
# Author    -   Karan Gupta
# Roll No.  -   2020PMD4224
# Degree    -   M.Tech (Mobile Computing and Data Analytics)
#########################################################

import os, sys, signal
def spawn(prog, *args):                                             # pass progname, cmdline args

    stdinFd = sys.stdin.fileno()                                    # get descriptors for streams
    stdoutFd = sys.stdout.fileno()                                  # normally stdin=0, stdout=1
    parentStdin, childStdout = os.pipe()                            # make two IPC pipe channels
    childStdin, parentStdout = os.pipe()                            # pipe returns (inputfd, outoutfd)
    pid = os.fork()                                                 # make a copy of this process
    if pid:
        os.close(childStdout)                                       # in parent process after fork:
        os.close(childStdin)                                        # close child ends in parent
        os.dup2(parentStdin, stdinFd)                               # my sys.stdin copy = pipe1[0]
        os.dup2(parentStdout, stdoutFd)                             # my sys.stdout copy = pipe2[1]
    else:
        os.close(parentStdin)                                       # in child process after fork:
        os.close(parentStdout)                                      # close parent ends in child
        os.dup2(childStdin, stdinFd)                                # my sys.stdin copy = pipe2[0]
        os.dup2(childStdout, stdoutFd)                              # my sys.stdout copy = pipe1[1]
        args = (prog,) + args
        os.execvp(prog, args)                                       # new program in this process
        assert False, 'execvp failed!'                              # os.exec call never returns here

if __name__ == '__main__':
    mypid = os.getpid()
    spawn('python3', 'pipetest-1.py', 'spam')                       # fork child program
    print('Hello 1 from parent', mypid)                             # to child's stdin
    sys.stdout.flush()                                              # subvert stdio buffering
    reply = input()                                                 # from child's stdout
    sys.stderr.write('Parent got: "%s"\n' % reply)                  # stderr not tied to pipe!
    i=2
    while True:
        try:
            if i==15:                                               # value at which you have to send End Message From Parent
                print("End")
                sys.stderr.write("Parent has sent 'End' Message\n")
                sys.exit(0)
            else:
                print('Hello',i,'from parent', mypid)

            sys.stdout.flush()                                      # subvert stdio buffering
            reply = sys.stdin.readline()                            # read the Latest Reply from the pipe
            if reply[:-1]=="Stop" or reply[:-1]=="End":
                sys.stderr.write('Parent got: "%s"\n' % reply[:-1])
                sys.exit()
            else:
                sys.stderr.write('Parent got: "%s"\n' % reply[:-1])
            i+=1
        except KeyboardInterrupt:                                   # for keyborad interrrupt
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)