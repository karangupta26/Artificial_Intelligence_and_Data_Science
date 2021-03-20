import rpyc
import sys

conn = rpyc.connect("localhost", 12345)

print("Welcom to Calculator - Remote Procedure call")
print("1. Addition")
print("2. Subtration")
print("3. Multiplication")
print("4. Divion")
while(True):
    choice=input(" Enter your operation with operands choice operand1 operand2 : ")
    ch=choice.split()
    if int(ch[0])==1:
        x = conn.root.add(int(ch[1]),int(ch[2]))
        print("Addition : ",x)
        
    elif int(ch[0])==2:
        x = conn.root.sub(int(ch[1]),int(ch[2]))
        print("subtraction : ",x)
    
    elif int(ch[0])==3:
        x = conn.root.mul(int(ch[1]),int(ch[2]))
        print("Multiplication : ",x)
    
    elif int(ch[0])==4:
        try:
            x = conn.root.div(int(ch[1]),int(ch[2]))
            print("Division : ",x)
        except ZeroDivisionError:
            print("Zero Division not Possible")
    
    else:
        print("Operation doesn't exist.")
        sys.exit()