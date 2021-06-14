import math
import sys
def decrypt_key(key):
    key=str(key)
    decrypt_key=[""]*len(key)
    for i in key:
        decrypt_key[int(i)-1]=str(key.index(i)+1)
    key="".join(decrypt_key)
    return int(key)

def read_encipher_matrix(strings,columns):
    cipher=[]
    for col in range(columns):
        cipher_str=""
        for string in strings:
            if string==strings[len(strings)-1] and len(string)<col+1:
                continue 
            else:
                cipher_str= cipher_str+string[col]
        cipher.append(cipher_str)
    return cipher 

def encrypt_columnar(plaintext,columns=None,key=None,transposition_type=None):
    cipher=""
    if transposition_type=="keylessColumnar":
        crypt_str=[]
        for i in range(0,len(plaintext),columns):
            string=plaintext[i:i+columns]
            crypt_str.append(string)
        
        cipher=read_encipher_matrix(crypt_str,columns)
        cipher="".join(encrypt for encrypt in cipher)
        
    if transposition_type=="keyedColumnar":
        crypt_str=[]
        columns=len(str(key)) 
        key=str(key)
        for i in range(0,len(plaintext),columns):
            string=plaintext[i:i+columns]
            crypt_str.append(string)
        
        temp_crypt_str=['']*columns
        for i in range(0,columns):
            for string in crypt_str:
                if string == crypt_str[len(crypt_str)-1] and (len(string)<i+1):
                    break
                else:
                    temp_crypt_str[int(key[i])-1]+=string[i]
            #print(temp_crypt_str)
            cipher=''.join(temp_crypt_str)

    if transposition_type=="doubletranspostion":
        cipher=encrypt_columnar(plaintext,key=key,transposition_type="keyedColumnar")
        cipher=encrypt_columnar(cipher,key=key,transposition_type="keyedColumnar")

    return cipher.replace(" ","")

def decrypt_columnar(ciphertext,columns=None,key=None,transposition_type=None):
    plaintext=""
    if transposition_type=="keylessColumnar":
        rows=int(math.ceil(len(ciphertext)/columns))
        plain_str=[""]*rows
        index=0
        for col in range(columns):
            for row in range(rows):
                if (row == rows-1) and (len(plain_str[row])==(len(ciphertext)%columns)):
                    continue
                else:
                    plain_str[row]=plain_str[row]+ciphertext[index]
                    index+=1

        for string in plain_str:
            plaintext = plaintext + string
    
    if transposition_type=="keyedColumnar":
        plain_str=[]
        key=str(key)
        row_index=0
        col_index=0
        column=len(key)
        rows=int(math.ceil(len(ciphertext)/column))
        cipher_index=0
        temp_plain_str=['']*column
        for i in range(0,column):
            for j in range(rows):
                if int(key[i])>int(len(ciphertext)%column) and (j==rows-1):
                    continue
                else:
                    temp_plain_str[int(key[i])-1]+=ciphertext[cipher_index]
                    cipher_index+=1
           
        for i in range(0,rows):
            
            for string in  temp_plain_str:
                if string==temp_plain_str[len(temp_plain_str)-1] and i+1>len(string):
                    break
                else:
                    plaintext+=string[i]
    
    if transposition_type=="doubletranspostion":
        plaintext=decrypt_columnar(ciphertext,key=key,transposition_type="keyedColumnar")
        plaintext=decrypt_columnar(plaintext,key=key,transposition_type="keyedColumnar")

    return plaintext.replace(" ","")
def encryptRailFence(text, key): 
  
    # create the matrix to cipher  
    # plain text key = rows ,  
    # length(text) = columns 
    # filling the rail matrix  
    # to distinguish filled  
    # spaces from blank ones 
    rail = [['\n' for i in range(len(text))] 
                  for j in range(key)] 
      
    # to find the direction 
    dir_down = False
    row, col = 0, 0
      
    for i in range(len(text)): 
          
        # check the direction of flow 
        # reverse the direction if we've just 
        # filled the top or bottom rail 
        if (row == 0) or (row == key - 1): 
            dir_down = not dir_down 
          
        # fill the corresponding alphabet 
        rail[row][col] = text[i] 
        col += 1
          
        # find the next row using 
        # direction flag 
        if dir_down: 
            row += 1
        else: 
            row -= 1
    # now we can construct the cipher  
    # using the rail matrix 
    result = [] 
    for i in range(key): 
        for j in range(len(text)): 
            if rail[i][j] != '\n': 
                result.append(rail[i][j]) 
    return("" . join(result)) 
      
# This function receives cipher-text  
# and key and returns the original  
# text after decryption 
def decryptRailFence(cipher, key): 
  
    # create the matrix to cipher  
    # plain text key = rows ,  
    # length(text) = columns 
    # filling the rail matrix to  
    # distinguish filled spaces 
    # from blank ones 
    rail = [['\n' for i in range(len(cipher))]  
                  for j in range(key)] 
      
    # to find the direction 
    dir_down = None
    row, col = 0, 0
      
    # mark the places with '*' 
    for i in range(len(cipher)): 
        if row == 0: 
            dir_down = True
        if row == key - 1: 
            dir_down = False
          
        # place the marker 
        rail[row][col] = '*'
        col += 1
          
        # find the next row  
        # using direction flag 
        if dir_down: 
            row += 1
        else: 
            row -= 1
              
    # now we can construct the  
    # fill the rail matrix 
    index = 0
    for i in range(key): 
        for j in range(len(cipher)): 
            if ((rail[i][j] == '*') and
               (index < len(cipher))): 
                rail[i][j] = cipher[index] 
                index += 1
          
    # now read the matrix in  
    # zig-zag manner to construct 
    # the resultant text 
    result = [] 
    row, col = 0, 0
    for i in range(len(cipher)): 
          
        # check the direction of flow 
        if row == 0: 
            dir_down = True
        if row == key-1: 
            dir_down = False
              
        # place the marker 
        if (rail[row][col] != '*'): 
            result.append(rail[row][col]) 
            col += 1
              
        # find the next row using 
        # direction flag 
        if dir_down: 
            row += 1
        else: 
            row -= 1
    return("".join(result)) 

def encryptKeylessColumnar(plaintext,no_of_columns):
    encrypted_text=""
    if len(plaintext)%2!=0:
        if plaintext[len(plaintext)-1]=='Z':
            plaintext=plaintext+'Q'
        else:
            plaintext=plaintext+'Z'
    no_of_rows=int(len(plaintext)/no_of_columns)
    matrix=[['\n']*no_of_columns]*no_of_rows

    index=0
    for i in range(no_of_columns):
        for j in range(no_of_rows):
        
            matrix[i][j]=plaintext[index]
            index+=1
    
    print(matrix)
    
    for j in range(no_of_columns):
        for i in range(no_of_rows):
            encrypted_text=encrypted_text+matrix[j][i]

    return encrypted_text
    
def main():
    print("Welcome to Keyed and Keyless Transpostion Cipher: ")
    print("1. Keyless - Railfence Cipher (Encryption and Decryption_")
    print("2. Keyless - Columnar Cipher (Encryption and Decryption)")
    print("3. Keyed - Columnar Cipher (Encryption and Decryption)")
    print("4. Keyed -  Double Transposition (Ciphers Encryption and Decryption)")

    while(1):
        choice= int(input("Enter your Choice from above Ciphers:"))

        if choice == 1:
            plaintext=str(input(" Enter a Message for in Encryption : ")).upper().replace(" ","")
            rows=int(input(" Enter No. of Rows for Encrytion : "))
            encrypted_text=encryptRailFence(plaintext,rows)
            print("\n Encrypted Text : ",encrypted_text)
            decrypted_text=decryptRailFence(encrypted_text,rows)
            print("\n Decrypted Text : ",decrypted_text)
        
        elif choice == 2:
            plaintext=str(input(" Enter a Message for in Encryption : ")).upper().replace(" ","")
            columns=int(input(" Enter No. of Columns for Encrytion : "))
            encrypted_text=encrypt_columnar(plaintext,columns=columns,transposition_type="keylessColumnar")
            print("\n Encrypted Text : ",encrypted_text)
            decrypted_text=decrypt_columnar(encrypted_text,columns=columns,transposition_type="keylessColumnar")
            print("\n Decrypted Text : ",decrypted_text)

        elif choice == 3:
            
            plaintext= str(input(" Enter a Message for Encryption : ")).upper().replace(" ","")
            encryption_key=int(input(" Enter a key for Encryption : "))
            encrypted_text=encrypt_columnar(plaintext,key=encryption_key,transposition_type="keyedColumnar")
            decryption_key=decrypt_key(encryption_key)
            print("\n Encrypted Text : ",encrypted_text)
            decrypted_text=decrypt_columnar(encrypted_text,key=decryption_key,transposition_type="keyedColumnar")
            print("\n Decrypted Text: ",decrypted_text)
            #print("Decryption Key",decryption_key)

        elif choice == 4:
            
            plaintext= str(input(" Enter a Message for Encryption : ")).upper().replace(" ","")
            encryption_key=int(input(" Enter a key for Encryption : "))
            encrypted_text=encrypt_columnar(plaintext,key=encryption_key,transposition_type="doubletranspostion")
            decryption_key=decrypt_key(encryption_key)
            print("\n Encrypted Text : ",encrypted_text)
            decrypted_text=decrypt_columnar(encrypted_text,key=decryption_key,transposition_type="doubletranspostion")
            print("\n Decrypted Text: ",decrypted_text.replace(" ",""))
        else:
            print("Invalid Choice Exitinig the Cryptosystem.")
            sys.exit()
    
if __name__=="__main__":
    main()