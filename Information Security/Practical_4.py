
# Practical 4 Playfair Cipher
########################################################
# Author    -   Karan Gupta
# Roll No.  -   2020PMD4224
# Degree    -   M.Tech (Mobile Computing and Data Analytics)
# Subject   -   Information Security
#########################################################

def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]
    
def locindex(c,keyMatrix): # Get location of each character
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(keyMatrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt(msg,keyMatrix):  # Encryption    
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    print("CIPHER TEXT:",end=' ')
    cipher=""
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i],keyMatrix)
        loc1=list()
        loc1=locindex(msg[i+1],keyMatrix)
        if loc[1]==loc1[1]:
            print("{}{}".format(keyMatrix[(loc[0]+1)%5][loc[1]],keyMatrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
            cipher = cipher + str(keyMatrix[(loc[0]+1)%5][loc[1]]) + str(keyMatrix[(loc1[0]+1)%5][loc1[1]])
        elif loc[0]==loc1[0]:
            print("{}{}".format(keyMatrix[loc[0]][(loc[1]+1)%5],keyMatrix[loc1[0]][(loc1[1]+1)%5]),end=' ')
            cipher = cipher + str(keyMatrix[loc[0]][(loc[1]+1)%5]) + str(keyMatrix[loc1[0]][(loc1[1]+1)%5])
        else:
            print("{}{}".format(keyMatrix[loc[0]][loc1[1]],keyMatrix[loc1[0]][loc[1]]),end=' ')    
            cipher = cipher + str(keyMatrix[loc[0]][loc1[1]]) + str(keyMatrix[loc1[0]][loc[1]])
        i=i+2   
    return cipher     
                 
def decrypt(msg,keyMatrix):  # Decryption
    print("PLAIN TEXT:",end=' ')
    i=0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i],keyMatrix)
        loc1=list()
        loc1=locindex(msg[i+1],keyMatrix)
        if loc[1]==loc1[1]:
            print("{}{}".format(keyMatrix[(loc[0]-1)%5][loc[1]],keyMatrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(keyMatrix[loc[0]][(loc[1]-1)%5],keyMatrix[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        else:
            print("{}{}".format(keyMatrix[loc[0]][loc1[1]],keyMatrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        

def main():
    print("Welcome to Playfair Cipher :")
    key=str(input("Enter key : ")).upper().replace(" ", "")
    result=list()
    for c in key: # Storing key
        if c not in result:
            if c=='J':
                result.append('I')
            else:
                result.append(c)
    flag=0
    for i in range(65,91): # Storing other character
        if chr(i) not in result:
            if i==73 and chr(74) not in result:
                result.append("I")
                flag=1
            elif flag==0 and i==73 or i==74:
                pass    
            else:
                result.append(chr(i))
    k=0
    keyMatrix=matrix(5,5,0) # Initialize matrix
    for i in range(0,5): # Making matrix
        for j in range(0,5):
            keyMatrix[i][j]=result[k]
            k+=1
    print("Enter the text for Encryption")
    msg=str(input(" ENTER MSG:")).upper().replace(" ", "")

    print("\nEncrypted Message :")
    cipher=encrypt(msg,keyMatrix)
    print("\nDecrypted CIpher :")
    decrypt(cipher,keyMatrix)

if __name__ == "__main__":
    main()
    
