import os

def parent_child():
    n1=os.fork()
    n2=os.fork()

    if n1 > 0 and n2 > 0:
        print("Parent process and id is : ",os.getpid())
        print(" n1 : ", n1," n2 : ",n2)
        print(" Parent id : ",os.getppid())
    
    elif n1==0 and n2 > 0:
        print("First Child and id is : ", os.getpid())
        print(" n1 : ", n1," n2 : ",n2)
        print(" Parent id : ",os.getppid())
    
    elif n1 > 0 and n2 == 0:
        print("Second Child and id is : ", os.getpid())
        print(" n1 : ", n1," n2 : ",n2)
        print(" Parent id : ",os.getppid())
    
    else:
        print("Grand-Child and id is : ", os.getpid())
        print(" n1 : ", n1," n2 : ",n2)
        print(" Parent id : ",os.getppid())

parent_child()
    
    