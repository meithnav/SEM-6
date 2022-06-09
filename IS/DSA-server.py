from hashlib import sha256
import math
import random
import socket

def key_generation(p, q):
    n = p*q
    e = 1
    z = int((p-1)*(q-1))
    while True:
        temp = random.randrange(2, z)
        if math.gcd(temp,z) == 1:
            e = temp
            break
    d=1
    while(True):
        if (e*d)%z == 1:
            break
        else:
            d += 1
    return [e, n], [d, n]

def encryption(text, key):
    e, n = key
    encrypted = []
    for i in text:
        encrypted.append(((ord(i)-32)**e)%n)
    return encrypted


host='127.0.0.1'
port=9001
s=socket.socket()

s.connect((host,port))
print("Key Request Sent")

kr1=s.recv(1024)
kr1=[int(i) for i in kr1.decode().split()]
print("Public Key Received:", kr1)

ks1, ks2 = key_generation(57, 73)
print("Public Key Sent:", ks1)
ks1 = str(ks1[0]) + ' ' + str(ks1[1])
s.send(ks1.encode())

message1 = input("\nEnter the message: ")
d1 = sha256(message1.encode()).hexdigest()
sig = encryption(d1, ks2)
c1 = encryption(message1, kr1)

print("\nMessage Digest:", d1)
print("\nDigital Signature:", sig)

msg = str(sig) + str(c1)
s.send(msg.encode())

print("\nMessage has been " + s.recv(1024).decode())

s.close()
