import sys
import numpy as np

def cipher_encryption(plain, key):
    plain2d = np.zeros([2,1])
    key2d = np.zeros([2,2])
    encryp_text = ""
    # Handle condition if the message length is odd.
    if len(plain)%2 == 1:
        plain = plain + '!'
        
    # Convert msg to matrices
    for i in range(len(plain)):
        plain2d[i,0] = (ord(plain[i])-65)
        
    # Convert key to 2x2
    k = 0
    for i in range(2):
        for j in range(2):
            key2d[i,j] = (ord(key[k])-65)
            k += 1

    print (key2d)
    print (plain2d)
    hill2d = np.matmul(key2d,plain2d)
    print(hill2d)
    
    for i in range(2):
            hill2d[i] = hill2d[i]%26
            temp = int(hill2d[i])
            encryp_text += chr(temp + 65)
    print(hill2d)
    
    # checking validity of the key
    # finding determinant
    #Enter code here>
    # finding multiplicative inverse and implementing steps to encrypt text
    print("Encrypted text: {}".format(encryp_text))
    return encryp_text

def cipher_decryption(cipher, key):
    decryp_text = ""
    cipher2d = np.zeros([2,1])
    key2d = np.zeros([2,2])
    multifound = False
    
    # Handle condition if the message length is odd.
    if len(cipher)%2 == 1:
        cipher = cipher + '!'
        
    # Convert msg to matrices
    for i in range(len(cipher)):
        cipher2d[i,0] = (ord(cipher[i])-65)
        
    # Convert key to 2x2
    k = 0
    for i in range(2):
        for j in range(2):
            key2d[i,j] = (ord(key[k])-65)
            k += 1
            
    # finding determinant
    det = key2d[0,0]*key2d[1,1] - key2d[0,1]*key2d[1,0]
    det = abs(det)
    print (det)
    
    # finding multiplicative inverse
    
    multi = 0
    while multifound == False: 
        multi += 1
        mod_sum = (det*multi)%26
        if mod_sum == 1:
            multifound = True
    print (multi)
    
    # adjugate matrix
    # swapping
    adj = key2d
    print(adj)
    adj[0,1] = -adj[0,1]
    adj[1,0] = -adj[1,0]
    adj[0,0] , adj[1,1] = adj[1,1] , adj[0,0]
    print(adj)
    for i in range(2):
        for j in range(2):
            if adj[i,j] < 0:
                adj[i,j] = 26 + adj[i,j]
    print(adj)
    
    # multiplying multiplicative inverse with adjugate matrix
    for i in range(2):
        for j in range(2):
            adj[i,j] = adj[i,j] * multi
    print(adj)
    
    # Calculate modulo
    for i in range(2):
        for j in range(2):
            adj[i,j] = adj[i,j]%26
    print(adj, "adj")
    print(cipher2d, "cyph")
    
    # Convert cipher to plaintext
    decryp2d = np.matmul(adj,cipher2d)
    print(decryp2d , "decrypt")
    for i in range(2):
            decryp2d[i,0] = decryp2d[i,0]%26
            decryp_text += chr(int(decryp2d[i,0]) + 65)
    print(decryp2d)
    print("Decrypted text: {}".format(decryp_text))
    return decryp_text

cipher_encryption("SE", "HILL")
cipher_decryption("YI", "HILL")