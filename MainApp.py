import random, math

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def mod_inverse(e, phi):
    for x in range(1, phi):
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

def get2primes(fileName):
    pFile = open(fileName, 'r')
    primeList = pFile.readlines()
    pFile.close()
    for i in range(len(primeList)): # every line has an extra \n
        primeList[i] = int(primeList[i])

    p = random.randint(0, len(primeList)-1)
    q = random.randint(0, len(primeList)-1)
    while(p==q):
        q = random.randint(0, len(primeList))

    p = primeList[p]
    q = primeList[q]

    return p, q

# p, q = get2primes("list.txt")    
p, q = 1021, 1559
n = p*q
e = 2
phi = (p-1)*(q-1)

while(e<phi):
    if(gcd(e, phi)==1):
        break
    else:
        e+=1

d = mod_inverse(e, phi)

message = input("enter ur text: ")
cipher = encrypt(message, e, n)
print(cipher)
decMsg = decrypt(cipher, d, n)
print(decMsg)