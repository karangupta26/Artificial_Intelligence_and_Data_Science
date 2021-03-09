# Practical 3 Vignere Cipher
########################################################
# Author    -   Karan Gupta
# Roll No.  -   2020PMD4224
# Degree    -   M.Tech (Mobile Computing and Data Analytics)
# Subject   -   Information Security
#########################################################

# Constant String with index
alpha_str='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# This function generates the Key in Cyclic Manner until its length is equal to text length
def generateKey(text,key):
    key = list(key) 
    if len(text) == len(key): 
        return(key) 
    else: 
        for i in range(len(text) - len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 

# Encryption Function 
def encrypt(text,key):
    encrypt_text=[]
    for i in range(len(text)):
        x=(alpha_str.index(text[i])+alpha_str.index(key[i]))%26
        encrypt_text.append(alpha_str[x])
    return "".join(encrypt_text)

# Decryption Function
def decrypt(cipher,key):
    decrypt_cipher=[]
    for i in range(len(cipher)):
        x=(alpha_str.index(cipher[i])-alpha_str.index(key[i])+26)%26
        decrypt_cipher.append(alpha_str[x])
    return "".join(decrypt_cipher)

# Main Method
def main():
    print("Welcome to Vignere Cipher:")
    string=str(input("Enter Yout text : ")).upper().replace(" ","")
    key=str(input("Enter a Key for Encryption and Decryption : ")).upper().replace(" ","")
    key = generateKey(string, key)
    cipher_text = encrypt(string,key) 
    print("Ciphertext : ", cipher_text) 
    print("Original/Decrypted Text : ",decrypt(cipher_text, key))  

if __name__ == "__main__":
    main()