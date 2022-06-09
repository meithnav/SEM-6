
def transposition():
    col=10

    def menu():
        option=0
        nonlocal col

        while(option != -1):

            print("\n **** MAIN MENU *****\n")
            print(" 1) ENCRYPT COLUMN TRANSPOSITION CIPER")
            print(" 2) DECRYPT COLUMN TRANSPOSITION CIPER")
            print("-1) EXIT")
            print(" ENTER YOUR OPTION : ", end='')
            option = int(input().strip())

            if option ==1:
                print("\n **** COLUMN TRANSPOSITION ENCRYPTION *****")
                # print("ENTER THE NO. OF COLUMNS : ", end='')
                col = int(input("ENTER THE NO. OF COLUMNS : ").strip())
                encrypt(col)

            elif option ==2:
                print("\n **** COLUMN TRANSPOSITION  DECRYPTION *****")
                col = int(input("ENTER THE NO. OF COLUMNS : ").strip())
                decrypt(col)
            elif option == -1:
                print("\n\n ***** EXIT *****")

            else:
                print("ENTER VALID OPTION!!")
    
    
    def encrypt(col):
        print("ENTER THE TEXT : ", end='')
        txt = input().strip()
        res=[]

        if len(txt)%col !=0 :
            r = col - len(txt)%col 
            txt +=' '*r
        print(txt,'|',len(txt))

        for i in range(col) :
            for j in range(i,len(txt) , col):
                res.append(txt[j])
            res.append('$')
            # print(res)

        print("ENCRYPTED : " , ''.join(res))


    def decrypt(col):
        print("ENTER THE TEXT : ", end='')
        txt = input().strip()

        arr = txt.split('$')
        res=[]
        print(arr)
        for i in range(len(arr[0])):
            for j in range(len(arr)-1):
                res.append(arr[j][i])


        print("DECRYPTED : " , ''.join(res))




    
    menu()
    # decrypt(3)
    # encrypt(3)



    
transposition()
