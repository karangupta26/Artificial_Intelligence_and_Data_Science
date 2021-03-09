# Practical 1 Affine Cipher
########################################################
# Author    -   Karan Gupta
# Roll No.  -   2020PMD4224
# Degree    -   M.Tech (Mobile Computing and Data Analytics)
# Subject   -   Information Security
#########################################################
def extendedGCD(num1, num2): 
  # Base Case  
  if num1 == 0 :   
      return num2,0,1
            
  gcd,x1,y1 = extendedGCD(num2%num1, num1)  
  # Update x and y using results of recursive call  
  x = y1 - (num2//num1) * x1  
  y = x1  
    
  return gcd,x,y 

def modinv(a, m): 
  gcd, x, y = extendedGCD(a, m) 
  if gcd != 1:
    print(" Enter a Valid Key for Encryption and Decryption") 
    exit() # modular inverse does not exist, simply None
  else: 
    return x % m 
 
def encrypt(text, key): 
  #E = (a*x + b) % 26
  encrypted_text=''
  for char in text.upper().replace(' ',''):
      num=((key[0]*(ord(char)-ord('A'))+key[1]) % 26)+ord('A')
      encrypted_text=encrypted_text+chr(num)

  return encrypted_text   

def decrypt(cipher, key):
  #D(E) = (a^-1 * (E - b)) % 26
  decrypted_text=''
  for char in cipher:
      num=(modinv(key[0],26)*((ord(char)-ord('A'))-key[1]))%26+ord('A')
      decrypted_text=decrypted_text+chr(int(num))
      
  return decrypted_text

# Driver Code to test the above functions 
def main(): 
  text = str(input("Please Enter a Plain Text For Encryption:"))
  key = [0,0] 
  for i in range(2):
    print("Enter your ",i+1," key value:")
    key[i]=int(input())

  # calling encryption function 
  enc_text = encrypt(text, key) 
  print(' Encrypted Text: {}'.format(enc_text)) 

  # calling decryption function 
  print(' Decrypted Text: {}'.format(decrypt(enc_text, key) )) 
  print(ord('V'))

if __name__ == '__main__': 
  main() 