# Practical 1 
########################################################
# Author    -   Karan Gupta
# Roll No.  -   2020PMD4224
# Degree    -   M.Tech (Mobile Computing and Data Analytics)
# Subject   -   Network and Web Security
#########################################################
# Library Import
import sys
import random
import math
from hashlib import sha256


# Utility Function
def hashFunction(message):
    hashed = sha256(message.encode("UTF-8")).hexdigest()
    return hashed

def is_prime(n):
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def extendedEuclidean(denominator, prime):
    if denominator == 0:
        return prime, 0, 1
    else:
        gcd, x, y = extendedEuclidean(prime % denominator, denominator)
        
        return gcd, y - math.floor(prime / denominator) * x, x #or gcd, y - (prime // denominator) * x, x

def genrateKeyPair():
    p = int(input("Input enter a prime no. p: "))
    q = int(input("Input enter a prime no. q: "))         
    
    if not (is_prime(p) & is_prime(q)):
        genrateKeyPair()

    n = p*q
    print("p X q = ",n)
    phin = (p-1)*(q-1)
    print("phi(n) = ",phin)
    e = int(input("Enter a Encryption key(e): "))

    inverse = extendedEuclidean(e,phin)

    if inverse[0] == 1:
        d = int(inverse[1])
        print("Decryption key(d) is: ",d)
    else:
        sys.exit("Multiplicative inverse for the given encryption key does not exist. Choose a different encrytion key ")


    return ((e,n),(d,n))

def sign(privateKey, message):
    key, n = privateKey
    
    numberRepr = [ord(char) for char in message]
    print("Number representation before encryption: ", numberRepr)
    signature = [pow(ord(char),key)%n for char in message]
    
    #Return the array of bytes
    return signature


def verify(publicKey, signature, recivedHash):

    key, n = publicKey

    #Generate the plaintext based on the signature and key using a^b mod m
    numberRepr = [pow(char, key)%n for char in signature]
    plain = [chr(int(pow(char, key)%n)) for char in signature]

    print("Decrypted number representation is: ", numberRepr)
    
    constructedMessage = ''.join(plain)
    print("Constructed Message = ",constructedMessage)
    constructedHash = hashFunction(constructedMessage)

    if recivedHash != constructedHash:
        print(recivedHash, " != ", constructedHash)
        print("Signature Breach!")
        return
    
    print(recivedHash, " = ", constructedHash)
    print("Verified")
    return 

def main():

    publicKey, privateKey = genrateKeyPair()
    message = input("Enter a Message for Signature: ")
    hashedMessage = hashFunction(message)
    signature = sign(privateKey,message)
    verify(publicKey, signature, hashedMessage)

if __name__ == "__main__":
    main()