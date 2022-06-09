
def ceaser():
    key=10

    def menu():
        option=0
        nonlocal key

        while(option != -1):

            print("\n **** MAIN MENU *****\n")
            print(" 1) ENCRYPT CEASER CIPER")
            print(" 2) DECRYPT CEASER CIPER")
            print("-1) EXIT")
            # print(" ENTER YOUR OPTION : ", end='')
            option = int(input(" ENTER YOUR OPTION : ").strip())

            if option ==1:
                print("\n **** CEASER CIPHER ENCRYPTION *****")
                # print("\n ENTER THE KEY VALUE : ", end='')
                key = int(input(" ENTER THE KEY VALUE :").strip())
                encrypt(key)

            elif option ==2:
                print("\n **** CEASER CIPHER DECRYPTION *****")
                key = int(input(" ENTER THE KEY VALUE :").strip())
                decrypt(key)
            elif option == -1:
                print("\n\n ***** EXIT *****")

            else:
                print(" ENTER VALID OPTION!!")


    
    def cipher(txt ,key):
        res=[]
        for ele in txt:
            if ele == " ":
                res.append('$')
            elif ele == '$' and key<0:
                res.append(' ')
            else:
               res.append(chr((ord(ele) - 97 + key)%26 + 97))

        if key>0:
            print(" ENCRYPTED : " , ''.join(res))
        if key <0:
            print(" DECRYPTED : " , ''.join(res))
        
    
    
    def encrypt(key):
        print(" ENTER THE TEXT : ", end='')
        txt = input().strip().lower()
        cipher( txt , key)



    def decrypt(key):
        print(" ENTER THE TEXT : ", end='')
        txt = input().strip().lower()
        cipher( txt , (-1)*key)


    
    menu()


    
ceaser()
