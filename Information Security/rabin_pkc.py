import sys
import math

alphastring='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rabinEncryption(public_key, plainText):
    
    cipherText=[]
    for i in range(len(plainText)):
        c = pow(alphastring.index(plainText[i]), 2) % public_key              # n == Public Key
        cipherText.append(c)
    return cipherText

def rabinDecryption(prime_p, prime_q, ciphertext):
    
    plainText=[]
    for i in range(len(ciphertext)):
        a1 =  int(pow(ciphertext[i], (prime_p+1) / 4) % prime_p)
        a2 =  int(-pow(ciphertext[i], (prime_p+1) / 4) % prime_p)
        b1 =  int(pow(ciphertext[i], (prime_q+1) / 4) % prime_q)
        b2 =  int(-pow(ciphertext[i], (prime_q+1) / 4) % prime_q)
        #print(a1, a2, b1, b2)
        p1 = chineseReminder(a1, b1, prime_p, prime_q)
        p2 = chineseReminder(a1, b2, prime_p, prime_q)
        p3 = chineseReminder(a2, b1, prime_p, prime_q)
        p4 = chineseReminder(a2, b2, prime_p, prime_q)
        plainText.append((p1, p2, p3, p4))
    
    for i in range(len(plainText)):
        print(plainText[i])
    
    return plainText

def chineseReminder(a, b, p, q):
    m = p * q
    m1 = int(m/p)
    m2 = int(m/q)
    
    inv_m1 = extendedEuclidean(m1, p)
    inv_m2 = extendedEuclidean(m2, q)
    
    inv_m1 = inv_m1[1]
    inv_m2 = inv_m2[1]
    
    result = ((m1 * a * inv_m1) + (m2 * b * inv_m2)) % m
    
    return result

def isPrime(n) : 
    
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True

def checkPrime():
    prime_p = int(input("Prime-Number (p) : "))
    prime_q = int(input("Prime-Number (q) : "))
            
    if isPrime(prime_p) and isPrime(prime_q):
        k = extendedEuclidean(prime_p, 4)
        k = k[1] % 4
        k1 = extendedEuclidean(prime_q, 4)
        k1 = k1[1] % 4
        if (k == k1 == 3) or (k == k1 == 1):
            return prime_p, prime_q 
        else:
            sys.exit("Prime numbers are not in the form of (4K + 3) or (4K + 1)")
    else:
        sys.exit("Unexpected Input !!! Atleast one input is not prime ...") 

def extendedEuclidean(inverse, prime):
    if inverse == 0:
        return prime, 0, 1
    else:
        gcd, x, y = extendedEuclidean(prime % inverse, inverse)
        return gcd, y - math.floor(prime / inverse) * x, x 
    
def keyGeneration(prime_p, prime_q, n):
    public_key = n
    private_key = (prime_q, n)    
    return public_key, private_key   
    
def main():
    print("\n\t\t\tRABIN ASYMMETRIC CRYPTOGRAPHY")
    
    plainText = str(input("Plain-Text : ")).upper().replace(" ","")
    
    prime_p, prime_q = checkPrime()
    
    public_key = prime_p * prime_q
    private_key = (prime_q, public_key) 
    print("\nPublic-Key : ",public_key)
    print("Private-Key : ",private_key)
    
    c = rabinEncryption(public_key, plainText) #n == PUBLIC KEY and c = CIPHER TEXT
    print("\nCipher-Text : ",c)
    
    decryptedMessage = rabinDecryption(prime_p, prime_q, c)
    
    
    
if __name__ == '__main__':
    main()