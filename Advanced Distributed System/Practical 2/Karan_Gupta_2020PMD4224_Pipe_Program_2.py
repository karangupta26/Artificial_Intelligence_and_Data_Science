# Practical 2 - Perform inter-process communication between TWO Child processes..
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
      
    # We will create 2 child process 
    # and using these file descriptor 
    # the child processes will write  
    # some text and other child process will 
    # read the text written by the sibling process 
    
    # Two Child Process
    n1 = os.fork() 
    n2 = os.fork()
      
    # n1 and n2 greater than 0 represents the parent process 
    if n1 > 0 and n2 > 0: 
        print("Parent Process and id is : ", os.getpid())
        print(" n1 : ",n1," n2 : ",n2)
        print(" Parent id : ",os.getppid())
        print(" My Children will talk, child 1 will say Hi to my Child 2")

        
    elif n1==0 and n2>0: 

        # Child Process 1
        # It will write message for Child Process 2

        os.close(r) 
        print("\nThis is First Child having id, ",os.getpid()," and having parent id as ",os.getppid())
        print(" I am written to my sibling process.")
        
        text = b"Hello child process 2 and I am your Sibling, Child process 1"
        os.write(w, text) 
        print(" Written text:", text.decode()) 
    
    elif n1 > 0 and n2 ==0 :

        # Child Process 2
        # It will read message from Child Process 1

        os.close(w)
        
        print("\nThis is Second Child having id, ",os.getpid()," and having parent id as ",os.getppid())
        print(" I am reading from my sibling process.")
      
        # Read the text written by Child process 1
        print(" Child 2 Process is reading message form child 1:") 
        r = os.fdopen(r) 
        print(" Read text:", r.read())
        print(" Greetings Accepted Sibling 1")
        
          
if __name__=='__main__':
    main()