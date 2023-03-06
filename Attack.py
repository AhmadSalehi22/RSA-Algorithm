import time

def decrypt(cipher, d, n):
    message = []
    for char in cipher:
        try:
            message.append(chr(pow(int(char), d, n)))
        except Exception:
            pass
    return (''.join(message))

def attack(n, e, message, cipher):
    start = time.time()
    for d in range(1, 2147483647):
        temp = decrypt(cipher, d, n)
        if temp==message:
            stop = time.time()
            rTime = stop-start
            rTime = round(rTime, 2)
            return d, rTime

n = 101100721
e = 10001
message = "ahmad"
cipher = [22971586, 81928209, 23984243, 22971586, 51009063]
d, rTime = attack(n, e, message, cipher)
print("private key:", d, "Time:", rTime)
attackedMessage = decrypt(cipher, d, n)
print(attackedMessage)
