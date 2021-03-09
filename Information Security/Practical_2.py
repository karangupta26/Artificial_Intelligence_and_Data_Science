# Practical 2 Hill Cipher
########################################################
# Author    -   Karan Gupta
# Roll No.  -   2020PMD4224
# Degree    -   M.Tech (Mobile Computing and Data Analytics)
# Subject   -   Information Security
#########################################################

# Hill Cipher
from math import *

# Constant String with index
alpha_str='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Returns modulo inverse of a with 
# respect to m using extended Euclid 
# Algorithm Assumption: a and m are 
# coprimes, i.e., gcd(a, m) = 1 

def modInverse(a): 
    a = a % 26
    for x in range(1, 26): 
        if ((a * x) % 26 == 1): 
            return x 
    return 1

# Method For transposing a Matrix
def transposeMatrix(m):
    result = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return result

# Method For getting Minor of a Matrix
def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

# Method for Getting Determinant
def getMatrixDeternminant(m):

    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

# Method For Inverse of any M X M Matrix with modulo 26 and inverse Determinant
def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    inverseDeterminant=modInverse(determinant)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[inverseDeterminant*m[1][1]%26, -1*inverseDeterminant*m[0][1]%26],
                [-1*inverseDeterminant*m[1][0]%26, inverseDeterminant*m[0][0]%26]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = (inverseDeterminant*cofactors[r][c])%26
    return cofactors

# Method For Genrating Key Matrix with help of Alpha String
def generateKeyMatrix(keyString):
    n=ceil(sqrt(len(keyString))) 
    key=[[0]*n for i in range(n)]
    index=0
    for i in range(n):
        for j in range(n):
            key[i][j]=alpha_str.index(keyString[index])
            index+=1
    return key

# Hill Cipher encryption
def encrypt(text,key):

    # Defining of Rows and Columns
    n=len(key)
    textColumn=ceil(len(text)/n)
    
    # Insertion of Bogus character as Z in The End
    if textColumn*n>len(text):
        extraChar=textColumn*n-len(text)
        text=text+(extraChar*'Z')
    
    # Defining 2 Matrix for Handling Plain Text and Cipher in Matrix Form
    textMatrix=[[0]*textColumn for i in range(n)]
    cipherMatrix=[[0]*textColumn for i in range(n)]
    
    # Intializing Plain Text Matrix
    index=0
    for i in range(textColumn):
        for j in range(n):
            textMatrix[j][i]=alpha_str.index(text[index])
            index+=1
    # Multiplying the Key Matrix with Plaintext Modulo 26 for Cipher Matrix
    for i in range(n):
        for j in range(textColumn):
            cipherMatrix[i][j]=0
            for k in range(n):
                cipherMatrix[i][j]+=(key[i][k]*textMatrix[k][j])
            cipherMatrix[i][j]=cipherMatrix[i][j]%26

    # Retriving the Cipher from Cipher Matrix
    cipher=""
    for i in range(textColumn):
        for j in range(n):
            cipher=cipher+alpha_str[cipherMatrix[j][i]]
    return cipher
# Hill Cipher Decryption
def decrypt(cipher,key):

    # Defining Rows and Columns
    n=len(key)
    cipherColumn=ceil(len(cipher)/n)

    # Defining 2 Matrix for Handling Plain Text and Cipher in Matrix Form
    cipherMatrix=[[0]*cipherColumn for i in range(n)]
    textMatrix=[[0]*cipherColumn for i in range(n)]
    
    # Intializing Cipher Text Matrix
    index=0
    for i in range(cipherColumn):
        for j in range(n):
            cipherMatrix[j][i]=alpha_str.index(cipher[index])
            index+=1

    # Operation On Key Matrix
    keyInverse=getMatrixInverse(key)

    # Multiplication of Key Matrix with cipher Matrix modulo 26
    for i in range(n):
        for j in range(cipherColumn):
            textMatrix[i][j]=0
            for k in range(n):
                textMatrix[i][j]+=(keyInverse[i][k]*cipherMatrix[k][j])
            textMatrix[i][j]=textMatrix[i][j]%26
    
    # Retriving the text from Text Matrix
    text=""
    for i in range(cipherColumn):
        for j in range(n):
            text=text+alpha_str[textMatrix[j][i]]
    return text

def main():
    print("Welcome to Hill Cipher")
    print("Please Enter a Key for Encryption and Decryption on Plain Text")
    key_str=str(input()).upper()
    if len(key_str) not in [4,9,16,25]:
        print("Please Enter a Key having a length of n^2 where n=[2,3,4,5]:")
        main()
    else:
        keyMatrix=generateKeyMatrix(key_str)
        det=getMatrixDeternminant(keyMatrix)
        modulo26det=det%26
        if det==0 or (modulo26det%2 == 0) or (modulo26det%13 == 0):
            print("Enter a Valid Key, Key Matrix is Not Inveritble or determinant has common factors with modular base.")
            main()
        else:
            plainText=str(input("Enter a Plain Text Which is to be Encrypted :")).upper().replace(" ","")
            
            print("\n\nFollowing is Encrpted Text:")
            cipherText=encrypt(plainText,keyMatrix)
            print(cipherText)
            print("\n\nFollowing is Decrypted Text of Above")
            print(decrypt(cipherText,keyMatrix))
        
if __name__ == "__main__":
    main()
