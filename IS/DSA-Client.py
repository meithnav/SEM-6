from hashlib import sha256
import math
import random
import socket

def key_generation(p, q):
    n = p * q
    e = 1
    z = int((p - 1) * (q - 1))
    while True:
        temp = random.randrange(2, z)
        if math.gcd(temp, z) == 1:
            e = temp
            break
    d = 1
    while (True):
        if (e * d) % z == 1:
            break
        else:
            d += 1
    return [e, n], [d, n]

def decryption(encrypted, key):
    d, n = key
    decrypted = ''
    for i in encrypted:
        decrypted += chr(((i**d) % n) + 32)
    return decrypted


host = '127.0.0.1'
port = 9001
s = socket.socket()

s.bind((host, port))
s.listen(1)
c, addr = s.accept()
print("Key Request Received")

kr1, kr2 = key_generation(13, 29)
print("Public Key Sent:", kr1)
kr1 = str(kr1[0]) + ' ' + str(kr1[1])
c.send(kr1.encode())

ks1 = c.recv(1024)
ks1 = [int(i) for i in ks1.decode().split()]
print("Public Key Received:", ks1)

msg = c.recv(1024)
sig, c1 = [i for i in msg.decode().split('][')]
sig = [int(i) for i in sig[1:].split(', ')]
c1 = [int(i) for i in c1[:-1].split(', ')]

print("\nReceived Digital Signature:", sig)
print("Received Ciphertext:", c1)

d1 = decryption(sig, ks1)
message2 = decryption(c1, kr2)
d2 = sha256(message2.encode()).hexdigest()

print("\nMessage digest recieved:", d1)
print("Message digest generated:", d2)

if d1 == d2:
    print('\nConnection secure')
    print('Message received:',message2)
    c.send('Accepted'.encode())
else:
    print('\nSecurity Compromised')
    c.send('Rejected'.encode())

c.close()
s.close()
