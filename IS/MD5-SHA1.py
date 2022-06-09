import hashlib

def verifySha1(payload):
    msg, d1 = payload.split(":")
    print("MSG RECEIVED : " ,msg)
    print("MSG DIGEST RECEIVED (D1): " ,d1)

    sha = hashlib.sha1(msg.encode())
    d2 = sha.hexdigest()

    if (d1 == d2):
        print("MSG AUTHENTICATED! ")
    else:
        print("MSG CORRUPTED! ")
 

def verifyMD5(payload):
    msg, d1 = payload.split(":")
    print("MSG RECEIVED : " ,msg)
    print("MSG DIGEST RECEIVED (D1): " ,d1)


    md5 = hashlib.md5(msg.encode())
    d2 = md5.hexdigest()

    if (d1 == d2):
        print("MSG AUTHENTICATED! ")
    else:
        print("MSG CORRUPTED! ")


def sha1(msg):
    print("\n\n***** SHA1 *****")
    sha1 = hashlib.sha1(msg.encode())
    d1 = sha1.hexdigest()
    payload = msg+":"+d1
    print("\n SHA1 PACKET :  "+payload)
    verifySha1(payload)

def md5(msg):
    print("\n\n***** MD5 *****")
    md5 = hashlib.md5(msg.encode())
    d2 = md5.hexdigest()
    payload = msg+":"+d2

    print(" MD5 PACKET :  ", payload)
    verifyMD5(payload)


def main():
    msg = "My name is Meith"

    sha1(msg)
    md5(msg)

main()