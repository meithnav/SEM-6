
import random
import numpy as np
import math

BIRTHDAY_MATCH = {}

def swap(A, i, j):
    A[i] , A[j] = A[j], A[i]

def randomiseArr(arr):

    for i in range(len(arr)-1 , 0 , -1):
        j = random.randint(0, i-1) 
        swap(arr, i, j)

    return arr


def genrateList(N, people):
    birthdays = []
    repeat=0

    while people>0:
        num = random.randint(1,N)

        if num not in BIRTHDAY_MATCH.keys():
            BIRTHDAY_MATCH[num]=1
            people-=1

        else: 
            if BIRTHDAY_MATCH[num]== 1:
                BIRTHDAY_MATCH[num]+=1
                birthdays.append(num)
                repeat+=1
                people-=1

    return repeat
    # return birthdays
    # return randomiseArr(birthdays)



def findMinN(p, N) -> int:
    return math.ceil(math.sqrt(2 * N * math.log(1/(1-p))))


def birthdayParadox(N, people,pairs_repeat, total_people):

    pairs = total_people*(total_people-1)/2
    unique_pairs = (N-1)/N
    chance_unique_pairs = (unique_pairs)**(pairs)
    chance_match = 1 - chance_unique_pairs
    pairs_repeat += genrateList(N, people)
    print("***** BIRTHDAY PARADOX ANALYSIS *****")
    print(" TOTAL NO. OF ITEMS : ", N, "\n NO. OF PEOPLE : ", total_people)
    print(" PROBABILITY OF SOME MATCH : {:.2%}".format(chance_match))
    print(" PROBABILITY OF ACTUAL MATCH : {:.2%}".format(2*pairs_repeat/total_people))

    return pairs_repeat

def menu():
    option=0
    while(option != -1):

        print("\n **** MAIN MENU *****\n")
        print(" 1) BIRTHDAY PARADOX ANALYSIS")
        print(" 2) MINIMUM PEOPLE REQUIRED FOR A CERTAIN PROBABILITY")
        print("-1) EXIT")
        option = int(input(" ENTER YOUR OPTION : ").strip())

        
        if option == -1:
            print("\n\n ***** EXIT *****")

        elif option ==1:
            print("\n ***** BIRTHDAY PARADOX *****")
            pairs_repeat=0
            total_people=0

            N = int(input(" ENTER THE NUMBER OF POSSIBLE ITEMS (Eg. DAYS) : "))
            people = int(input(" ENTER THE NUMBER OF PEOPLE : "))
            total_people+=people
            pairs_repeat = birthdayParadox(N, people,pairs_repeat, total_people)

            while True:
                print("\n ENTER -1 TO END BIRTHDAY PARADOX ANALYSIS")
                people = int(input(" ENTER MORE NUMBER OF PEOPLE : "))

                if people <1:
                    break

                total_people +=people
                if total_people >= N:
                    print(" TOTAL NO. OF ITEMS : ", N, "\n NO. OF PEOPLE : ", total_people)
                    print("\n NO. OF PEOPLE IN THE ROOM HAS EXCEEDED ITEMS. SO, 100% PROBABILITY OF COLLISION.")
                    break

                pairs_repeat = birthdayParadox(N, people, pairs_repeat, total_people)



        elif option ==2:
            print("\n ***** FIND THE MIN PEOPLE *****")
            p = float(input(" ENTER THE PROBABILITY : "))
            print(" MINIMUM OF {} PEOPLE ARE REQUIRED FOR {:.2%} PROBABILITY CHANCES OF ATLEAST ONE PAIR COINCIDING.".format(findMinN(p, 365) ,p ))

       
        else:
            print("ENTER VALID OPTION!!"  )  



menu()


