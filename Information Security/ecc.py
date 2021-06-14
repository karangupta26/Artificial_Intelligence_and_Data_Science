import sys
import random
import math
from fractions import Fraction 

def checkPrime():
    
    flag = False
    prime = int(input("Prime-Number [GF(prime)] : "))
    if prime > 1:
        for itr in range(2, prime):
            if (prime % itr) == 0:
                flag = True
                break
    if flag == True:
        sys.exit("Error ... Expected value is not a prime number !!! ") 
    else:
        return prime
    
def findPoints(modulo, a, b):
    pointList = [] 
    
    for x in range(0, modulo):
        point_x = (pow(x, 3) + a * x + b) % modulo
        
        for y in range(0, modulo):
            point_y = pow(y, 2) % modulo
            
            if(point_x == point_y):
                pointList.append((x, y))
            else:
                continue
    
    print("\nCurve Equation points : ",pointList) 
    '''
    remove(a,0) type of element(s) as it may give fraction a/0 issue
    '''
    for x in pointList:
        if(x[1] == 0):
            pointList.remove(x)
            
    e1 = (4,2)
    
    return e1

def addPoints(randomInt, e1):
    #e1 = (2, 22)
    x = temp_x = e1[0]
    y = temp_y = e1[1]
    
    temp_e = samePoint(x, y, x, y)
    temp_x = temp_e[0]
    temp_y = temp_e[1]
    
    for add in range(0, randomInt-2):
        if(e1 == temp_e):
            temp_x, temp_y = samePoint(temp_x, temp_y, x, y)
            temp_e = (temp_x, temp_y)
            
        else:
            temp_x, temp_y = differentPoint(temp_x, temp_y, x, y)
            temp_e = (temp_x, temp_y)
    e2 = temp_e
    
    return e2

def samePoint(x1, y1, x2, y2):
    if y1 == 0:
        sys.exit("Error !!! Denominator is 0")
    lambda_eq = Fraction((3 * pow(x1, 2) + 2) , (2 * y1)) #Fraction(a / b)
    print("\n")
    print("X :", x1 , "," , "Y :", y1,  "," , "X :", x2, "," , "Y :", y2)
    print("Lambda : ",lambda_eq)
    lambda_cal = extendedEuclidean(Fraction(lambda_eq).denominator, 67)
    print("Inverse:", lambda_cal[1])
    lambda_cal = (Fraction(lambda_eq).numerator * lambda_cal[1])
    
    x = (pow(lambda_cal,2) - x1 - x2) % 67
    print("X : ",x)
    y = (lambda_cal * (x1 - x) - y1) % 67
    print("Y : ",y)
    
    return x, y

def differentPoint(x1, y1, x2, y2):
    if x2 == x1:
        sys.exit("Error !!! Denominator is 0")
    lambda_eq = Fraction((y2 - y1), (x2 - x1))#Fraction(a / b)
    print("\n")
    print("X :", x1 , "," , "Y :", y1,  "," , "X :", x2, "," , "Y :", y2)
    print("Lambda : ",lambda_eq)
    
    lambda_cal = extendedEuclidean(Fraction(lambda_eq).denominator, 67)
    print("Inverse:", lambda_cal[1])
    lambda_cal = (Fraction(lambda_eq).numerator * lambda_cal[1])
    #print(lambda_cal)
    
    x = (pow(lambda_cal,2)- x1 - x2) % 67
    print("X : ",x)
    
    y = (lambda_cal * (x1 - x) - y1) % 67
    print("Y : ",y)
    return x, y

def inversePoint(modulo, x1, y1):
    #print(y1)
    y1 = -y1 % modulo
    #print(y1)
    additiveInverse = (x1, y1)
    print((x1, y1))
    
    return additiveInverse

def extendedEuclidean(denominator, prime):
    if denominator == 0:
        return prime, 0, 1
    else:
        gcd, x, y = extendedEuclidean(prime % denominator, denominator)
        
        return gcd, y - math.floor(prime / denominator) * x, x #or gcd, y - (prime // denominator) * x, x

def eccEncryption(plainText, r, e1, e2):
    print("\n..... CALCULATING (c1) .....")
    c1 = addPoints(r, e1)
    
    print("\n..... CALCULATING (c2) .....")
    interimCal = addPoints(r, e2) # c2 = P + r * e2, where intermiCal = r * e2
    
    if (plainText == interimCal):
        x, y = samePoint(plainText[0], plainText[1], interimCal[0], interimCal[1])
    else:    
        x, y  = differentPoint(plainText[0], plainText[1], interimCal[0], interimCal[1])
    c2 = (x, y)
    return c1, c2

def eccDecryption(prime, d, c1, c2):
    
    intermiCal = addPoints(d, c1)
    additiveInverse = inversePoint(prime, intermiCal[0], intermiCal[1]) 
    if (c2 == additiveInverse):
        p1, p2 = samePoint(c2[0], c2[1], additiveInverse[0], additiveInverse[1])
    else:
        p1, p2 = differentPoint(c2[0], c2[1], additiveInverse[0], additiveInverse[1])

    return p1, p2

def main():
    print("\n\t\t\tELLIPTICAL-CURVE ASYMMETRIC CRYPTOGRAPHY")
    
    p1, p2 = input("Plain-Text : ").split()
    plainText = (int(p1), int(p2))
    
    a, b = input("Coefficients a & b : ").split()
    print("Curve Equation: y^2 = x^3 +",a,"x +",b)
    
    prime = checkPrime()
    e1 = findPoints(prime, int(a), int(b))
    print("\nRandom-point on the curve (e1): ",e1)
    d = int(input("Random-integer (d) : "))
    e2 = addPoints(d, e1)
    print("\nSecond point (e2) on the curve by solving (d * e1) :", e2)
    
    r = int(input("Random-number (r) : "))
    
    c1, c2 = eccEncryption(plainText, r, e1, e2)
    print("\nCipher-Text :", (c1, c2))
    
    p1, p2 = eccDecryption(prime, d, c1, c2)
    print("\nDecipher-Text :", (p1, p2))
    
if __name__ == '__main__':
    main()