
def myAlgo():
    key=''

    def menu():
        option=0
        nonlocal key

        while(option != -1):

            print("\n **** MAIN MENU *****\n")
            print(" 1) ENCRYPT DATA")
            print(" 2) DECRYPT DATA")
            print("-1) EXIT")
            print(" ENTER YOUR OPTION : ", end='')
            option = int(input().strip())

            if option ==1:
                print("\n **** ENCRYPTION *****")
                print("\n ENTER THE KEY VALUE : ", end='')
                key = input().strip()
                encrypt(key)

            elif option ==2:
                print("\n **** DECRYPTION *****")
                print("\n ENTER THE KEY VALUE : ", end='')
                key = input().strip()
                decrypt(key)

            elif option == -1:
                print("\n\n ***** EXIT *****")

            else:
                print(" ENTER VALID OPTION!!")

        
    def keyHash(key)-> int:
        val = 0 
        for ele in key: 
            val+= ord(ele)

        return val% len(key)

    def keyEnc(key, val)-> str:
        items = list(key)
        # print(items)
        for i in range(len(items)): 
            k = ord(items[i]) %3

            if k==0 : 
                items[i] = chr((ord(items[i]) - 97 +val)%26  +97)
            elif k==1:
                items[i] =  chr((ord(items[i]) - 97 -val )%26 +97)


        return "".join(items)

    def textHash(txt, n)-> int:  
        val = 0 
        for ele in txt: 
            val+= ord(ele)

        return val% n

    def Sbox(txt, val1) -> list:
        items = list(txt)
        n= len(txt) 
        if val1 %2 == 0 : # val1 == EVEN
            start = n-2 if n%2==0 else n-1
            temp = items[start] 
            for i in range(start,0, -2):
                items[i] = items[i-2]
                
            items[0]= temp

            for i in range(1, n ,2):
                items[i] = chr((ord(items[i]) - 97 +val1)%27  +97)

        else: # val1 == ODD
            start = n-1 if n%2==0 else n-2
            temp = items[start] 
            for i in range(start,1, -2):
                items[i] = items[i-2]

            items[1]= temp

            for i in range(0, n ,2):
                items[i] = chr((ord(items[i]) - 97 +val1)%27  +97)

        
        # print("STR MOVED and ADDED : ",items)
        return items[::-1]


    def readColswise(arr, lenKey)-> str:
        ct=''
        for i in range(lenKey):
            order = 1 if i%2==0 else -1
            ct+=  ''.join(arr[i][::order])

        return ct

    def  Pbox(sArr , encKey) -> str:
        padd = len(sArr) %len(encKey)
        if padd != 0:
            sArr += ['-']*(len(encKey) - padd)

        # print("PADDED str:",sArr)
        arr = []
        for j in range(len(encKey)):
            ls =[]
            for i in range(j , len(sArr) , len(encKey)):
                ls.append(sArr[i])
            arr.append(ls)

        # print("MATRIX BOX:",arr)
        ct = readColswise(arr , len(encKey))
        # print("COLUMNAR :",ct)
        return ct


    def inversePbox(txt, encLen, depth ):
        arr=[]
        for i in range(0, len(txt), depth):
            order = 1 if (i//depth)%2==0 else -1
            arr.append(txt[i:i+depth])
            arr[-1] = arr[-1][::order]
        # print(arr)

        invTxt = ''
        for i in range(depth):
            line=''
            for j in range(encLen):
                line += arr[j][i]

            invTxt += line
        # print(invTxt)
        return invTxt.split("-")[0][::-1]


    def inverseSbox(txt , val1):
        items = list(txt)
        n= len(txt) 
        if val1 %2 == 0 : # val1 == EVEN
            end = n-2 if n%2==0 else n-1
            temp = items[0] 
            for i in range(0, len(txt)-2 ,2):
                items[i] = items[i+2]
                
            items[end]= temp

            for i in range(1, n ,2):
                items[i] = chr((ord(items[i]) - 97 -val1)%27  +97)

        else: # val1 == ODD
            end = n-1 if n%2==0 else n-2
            temp = items[1] 
            for i in range(1, len(txt)-2, 2):
                items[i] = items[i+2]

            items[end]= temp

            for i in range(0, n ,2):
                items[i] = chr((ord(items[i]) - 97 -val1)%27  +97)

        # print("INVERSE S-BOX :", "".join(items))
        return "".join(items)

    
    def encrypt(key):

        val = keyHash(key)
        encKey = keyEnc(key, val)
        print(" ENTER THE TEXT : ", end='')
        txt = input().strip().lower()
        txtF = txt.replace(" ", "{")
        val1 = textHash(txtF ,len(key))
        sArr=  Sbox(txtF , val1)

        # print("S-BOX : ", sArr)
        ct = Pbox(sArr , encKey)
        # print("P-BOX : ", ct)
        final_ct = ct+"$"+str(val1)
        print(" CIPHERED TEXT : ", final_ct)
        print(" KEY USED : ",key )


    def decrypt(key):
        val = keyHash(key)
        encKey = keyEnc(key, val)
        print(" ENTER THE CIPHERED TEXT : ", end='')
        ct = input().strip().lower()
        txt = ct.split("$")[0]
        val1 = int(ct.split("$")[1])
        s = inversePbox(txt, len(encKey), len(txt)//len(encKey))
        # print("INVERSE P-BOX :", s)
        invStxt=  inverseSbox(s , val1)
        pt = invStxt.replace("{", " ")
        print(" DECIPHERED TEXT :", pt)
      
    
    menu()



myAlgo()

