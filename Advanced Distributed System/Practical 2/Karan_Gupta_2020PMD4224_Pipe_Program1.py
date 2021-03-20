# Practical 2 - Perform inter-process communication between a Parent and Child process.
########################################################
# Author    -   Karan Gupta
# Roll No.  -   2020PMD4224
# Degree    -   M.Tech (Mobile Computing and Data Analytics)
#########################################################
  
# importing os module  
import os 
  
def main():
  
    # Creating a pipe 
    # returns file descriptors r and w
    # which can be used for both reading and writting. 
    r, w = os.pipe() 
      
    # We will create a child process 
    # and using these file descriptor 
    # the parent process will write  
    # some text and child process will 
    # read the text written by the parent process 
      
    # Create a child process 
    n = os.fork() 
      
    # n greater than 0 represents the parent process 
    if n > 0: 
      
        # Parent process  
        # Closes file descriptor r 
        os.close(r)
      
        # Write some text to file descriptor w  
        print("Parent process is writing") 
        text = b"Hello child process"
        os.write(w, text) 
        print("Written text:", text.decode()) 
      
          
    else: 
        # Child process  
        # Closes file descriptor w 
        os.close(w) 
      
        # Read the text written by parent process 
        print("\nChild Process is reading") 
        r = os.fdopen(r) 
        print("Read text:", r.read())

if __name__=='__main__':
    main()