import random

class Diffie:

    def __init__(self):
        self.P = 199
        self.alpha = self.primRoot(self.P)
        self.private_sender = self.privateKey(self.P)
        self.private_receiver = self.privateKey(self.P)
        self.public_sender = self.publicKey(self.P, self.private_sender , self.alpha)
        self.public_receiver = self.publicKey(self.P, self.private_receiver , self.alpha)
        self.display()


    def primRoot(self ,P):
        roots=[]
        base =2
        while base < P and len(roots) < P-1:
            for i in range(1, P):
                rem = base**i % P

                if rem in roots:
                    # print(base ,' : ', roots)
                    roots=[]
                    base+=1
                    break
                else: 
                    roots.append(rem)
        # print('FINAL : ', roots)
        return base

    
    def privateKey(self, P ):
        return  random.randint(2 , P-1)


    def publicKey(self, P, private , alpha):
        return  alpha**private % P


    def verify(self):
        k1 = self.public_receiver**self.private_sender % self.P
        k2 = self.public_sender**self.private_receiver % self.P
        print("SECRET KEY ")
        print("K1 : ", k1 ,'  K2 : ', k2)


    def display(self):
        print("\n\n*****  RESULTS *****\n")
        print("P : " , self.P)
        print("ALPHA : " , self.alpha)
        print("\nSENDER PRIVATE : " , self.private_sender)
        print("SENDER PUBLIC : " , self.public_sender)
        print("\nRECEIVER PRIVATE : " , self.private_receiver)
        print("RECEIVER PUBLIC : " , self.public_receiver)
        self.verify()


dh = Diffie()


