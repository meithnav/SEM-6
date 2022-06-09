import random
import math
class RSA: 

    def __init__(self) :
        self.p = 137
        self.q=149
        self.n = self.p * self.q
        self.window =len(str(self.n))
        self.z = (self.p-1)*( self.q-1)
        # print("n : ",self.n, "\nz : ", self.z)
        self.main()


    def E_GCD(self ,z):

        for i in range(2, z):
            if math.gcd(z,i) == 1:
                self.e = i
                # print("e : ", i)
                return
                # return i 
        

    def modifiedE_GCD_Target(self ,z):

        start = random.randint(2, z//2) 
        for i in range(start , z):
            if math.gcd(z,i) == 1:
                self.eT = i
                print("e : ", i)
                return
                # return i 

    def modifiedE_GCD_Sender(self ,z):

        start = random.randint(2, z//2) 
        for i in range(start , z):
            if math.gcd(z,i) == 1:
                self.eS = i
                print("e : ", i)
                return
                # return i 

    def createPrivate(self):
        d=1
        while True:
            if (d*self.e)%self.z == 1:
                    self.d=d
                    # print("d : ", d)
                    return 
            
            d+=1

    def createPrivate_Sender(self):
        d=1
        while True:
            if (d*self.eS)%self.z == 1:
                    self.dS=d
                    return 
            d+=1

    def createPrivate_Target(self):
        d=1
        while True:
            if (d*self.eT)%self.z == 1:
                    self.dT=d
                    return 
            d+=1
        
       
    def encryptData(self, pt):
        ct=[]
        for ele in pt:
            s = str((ord(ele)**self.e) %self.n )
            if len(s)%self.window !=0:
                pad = self.window - len(s)%self.window
                s = '0'*pad + s

            ct.append(s)

        return ''.join(ct)

    
    def modifiedEncryptData(self, pt):
        ct=[]

        # Enc with private of sender
        for ele in pt:
            s = (ord(ele)**self.eS) %self.n
            ct.append(s)
        # print("CT Sender : ", ct)


        # Enc with public of target
        ct_final=[]
        for ele in ct:
            s = str((ele**self.dT) %self.n )
            if len(s)%self.window !=0:
                pad = self.window - len(s)%self.window
                s = '0'*pad + s

            ct_final.append(s)

        # print("CT : ", ct_final)

        return ''.join(ct_final)

    
    def decryptData(self, ct):
        pt=[]

        for i in range(0,len(ct) , self.window):
            s = int(ct[i:i+self.window])
            p= (s**self.d) %self.n
            pt.append(chr(p))
            
        # print(pt)
        return ''.join(pt)


    def modifiedEcryptData(self, ct):
        pt=[]
        # Decryption using private of target
        for i in range(0,len(ct) , self.window):
            s = int(ct[i:i+self.window])
            p= (s**self.eT) %self.n
            pt.append(p)
        
        # print("DECIPHERED :", pt)


        # Decryption using public of sender
        pt_final=[]
        for ele in pt:
            p= (ele**self.dS) %self.n
            pt_final.append(chr(p))
        
        # print("DECIPHERED FINAL :", pt_final)
        return ''.join(pt_final)



    def menu(self):
        option=0
        while(option != -1):

            print("\n **** MAIN MENU *****\n")
            print(" 1) ENCRYPT DTA")
            print(" 2) DECRYPT DTA")
            print("-1) EXIT")
            option = int(input(" ENTER YOUR OPTION : ").strip())

            if option ==1:
                print("\n **** ENCRYPT DTA *****\n")
                data = input(" ENTER YOUR DATA : ").strip()
                # encData = self.encryptData(data)
                encData = self.modifiedEncryptData(data)
                print("CIPHERED TEXT : " , encData)

            elif option ==2:
                print("\n **** DECRYPT DTA *****\n")
                data = input(" ENTER YOUR CIPHERED TEXT : ").strip()
                # decData = self.decryptData(data)
                decData = self.modifiedEcryptData(data)
                print("DECIPHERED TEXT : " , decData)

            elif option == -1:
                print("\n\n ***** EXIT *****")

            else:
                print("ENTER VALID OPTION!!"  )  


    def main(self):
        # self.modifiedE_GCD(self.z)
        # self.createPrivate()
        self.modifiedE_GCD_Target(self.z)
        self.modifiedE_GCD_Sender(self.z)
        self.createPrivate_Sender()
        self.createPrivate_Target()
        self.menu()

    

rsa = RSA()

