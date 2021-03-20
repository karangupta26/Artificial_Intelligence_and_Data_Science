# Python3 program to explain os.mknod() method 
  
# importing os module 
import os,sys,time
  
# importing stat module 
import stat 
  
  
# Path 
path = "file.log"

if not os.path.exists(path):
    # Permission to use 
    per = 0o600
    
    # type of node to be created  
    node_type = stat.S_IRUSR  
    mode = per | node_type 
    
    # Create a file sytem node 
    # with specified permission 
    # and type using 
    # os.mknod() method 
    os.mknod(path, mode) 
    print("Filesystem node is created successfully")
try:
    while(True):

        # Read Process
        pipe=os.open(path,os.O_RDONLY)
        string=os.read(pipe,100)
        os.close(pipe)
        if string.decode("UTF-8").upper()=="STOP" or string.decode("UTF-8").upper()=='KEY IS PRESSED':
            print("*Message from Client : ",string.decode("UTF-8"))
            sys.exit()
        else:
            print("*Message from Client : ",string.decode("UTF-8"))
        
        # Writting Process
        pipe=os.open(path,os.O_WRONLY|os.O_TRUNC)
        input_msg=str(input("Enter a Msg from Server : "))
        b=str.encode(input_msg)
        if input_msg=="Stop":
            os.write(pipe,b)
            os.close(pipe)
            sys.exit()
        else:
            os.write(pipe,b)
            os.close(pipe)
        
        time.sleep(15)
    raise KeyboardInterrupt
except KeyboardInterrupt:
    print("Key is pressed. Exiting the program")
    pipe=os.open(path,os.O_WRONLY|os.O_TRUNC)
    input_msg='Key is Pressed'
    b=str.encode(input_msg)
    os.write(pipe,b)
    os.close(pipe)
    sys.exit()
    