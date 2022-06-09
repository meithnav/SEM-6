
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
        
 

    def createPrivate(self):
        d=1
        while True:
            if (d*self.e)%self.z == 1:
                    self.d=d
                    # print("d : ", d)
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
        # print("CT : ", ct)
        return ''.join(ct)

    
    def decryptData(self, ct):
        pt=[]

        for i in range(0,len(ct) , self.window):
            s = int(ct[i:i+self.window])
            p= (s**self.d) %self.n
            pt.append(chr(p))
            
        # print(pt)
        return ''.join(pt)


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
                encData = self.encryptData(data)
                print("CIPHERED TEXT : " , encData)

            elif option ==2:
                print("\n **** DECRYPT DTA *****\n")
                data = input(" ENTER YOUR CIPHERED TEXT : ").strip()
                decData = self.decryptData(data)
                print("DECIPHERED TEXT : " , decData)

            elif option == -1:
                print("\n\n ***** EXIT *****")

            else:
                print("ENTER VALID OPTION!!"  )  


    def main(self):
        self.E_GCD(self.z)
        self.createPrivate()
        self.menu()

    

rsa = RSA()

