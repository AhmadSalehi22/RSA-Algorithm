import random, math

startNum = 10000

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def mod_inverse(e, phi):
    for x in range(startNum, phi):
        if (e * x) % phi == 1:
            return x
    return -1

def encrypt(message, e, n):
    cipher = []
    for char in message:
        cipher.append(pow(ord(char), e, n))
    return cipher

def decrypt(cipher, d, n):
    message = []
    for char in cipher:
        message.append(chr(pow(int(char), d, n)))
    return (''.join(message))

def calcE(phi):
    e = startNum
    while(e<phi):
        if(gcd(e, phi)==1):
            return e
        else:
            e+=1
    
p, q = 10007, 10103
n = p*q
phi = (p-1)*(q-1) 
e = calcE(phi)
d = mod_inverse(e, phi)

print("p:",p)
print("q: ",q)
print("n: ",n)
print("e: ",e)
print("d: ",d)

message = "ahmad"
cipher = encrypt(message, e, n)
print(cipher)
decryptedMessage = decrypt(cipher, d, n)
print(decryptedMessage)