
import random
import numpy as np

INTERVIEW_COST = 50
FIRE_COST = 0.5
DAILY_COST = 1.5

# SKILlS
#  0: HTML , 1: ENGLISH , 2: EXCEL, 3: PYTHON , 4: TAXATION , 5: AGILE 

# POSTS
# 0 -> WEB DEV , 1-> MANAGER , 2-> ACCOUNTANT , 3 -> ML 

SKILLS = 6
post_list=  ["WEB DEV" , "MANAGER" , "ACCOUNTANT" , "MAINTENANCE"]
skills_list = ["HTML" , "ENGLISH" , "EXCEL" , "PYTHON" , "TAXATION", "AGILE"]
METRIC = [
    [0.6 , 0.05,  0.05 , 0.3 ,0 , 0.3],
    [0.1, 0.4, 0.2, 0.05, 0.1, 0.4 ],
    [0, 0.4, 0.2, 0.05, 0.1, 0.4 ],
    [0.1, 0.1, 0.1, 0.6, 0, 0.2 ],
]

BEST_INDEX = [-1]*len(post_list)
BEST_INDEX_SCORE = [-1]*len(post_list)


def swap(A, i, j):
    A[i] , A[j] = A[j], A[i]

def randomiseArr(arr):

    for i in range(len(arr)-1 , 0 , -1):
        j = random.randint(0, i-1) 
        swap(arr, i, j)

    return arr


def CalcScore(option , candidates):
    scores=[]
    
    for i in range(len(candidates)):
        scores.append(np.dot(candidates[i], METRIC[option]))

    return scores


def genratePerson():
    skills = []
    for i in range(SKILLS):
        skills.append(random.randint(0,100))

    return skills


def genrateList(n):
    candidates = []
    for i in range(n):
        candidates.append(genratePerson())

    return candidates
    # return randomiseArr(candidates)




def hiringOld(scores):
    print(" **** HIRING PROBLEM ****")
    NO_CANDIDATE = 100
    candidates = genratePerson(NO_CANDIDATE)
    # best = candidates[0]
    best_index = 0
    TOTAL_COST = 0

    for i in range(len(candidates)) :

        if candidates[best_index] <candidates[i]:
            best_index = i
            TOTAL_COST += (FIRE_COST*BEST_INDEX_SCORE + DAILY_COST*scores[i])

        TOTAL_COST += (DAILY_COST*scores[i] +INTERVIEW_COST)

    print(" TOTAL COST :", TOTAL_COST)
    print(" BEST EMPLOYEE ID : ", best_index )



def hiring(scores, option):
    # best_index = 0
    TOTAL_COST = 0

    for i in range(len(scores)) :
        if BEST_INDEX_SCORE[option] <scores[i]:
            BEST_INDEX_SCORE[option] = scores[i]
            BEST_INDEX[option] = i
            TOTAL_COST += (FIRE_COST*BEST_INDEX_SCORE[option] + DAILY_COST*scores[i])

        TOTAL_COST += (DAILY_COST*scores[i] +INTERVIEW_COST)

    print(" TOTAL COST FOR ",post_list[option] ," PROCESS :", TOTAL_COST)
    print(" BEST EMPLOYEE ID :", BEST_INDEX[option] )


def DisplayEmp():

    print("\n **** COMPANY EMPLOYEES ****\n")
    print("POSITION \t   EMP ID\t    SCORE")
    print("-"*45)

    for i in range(len(BEST_INDEX)):
        if BEST_INDEX[i] == -1 :
            print(post_list[i]," \t   UNASSINGED  \t      -" )
        else:
            print(post_list[i], " \t  ", BEST_INDEX[i], ' '*(5- len(str(BEST_INDEX[i]))%5 ),"\t   ", round(BEST_INDEX_SCORE[i] ,3))

def menu():

    option=0
    while(option != -1):

        print("\n **** MAIN MENU *****\n")
        print(" 1) WEB DEVELOPER")
        print(" 2) MANAGER")
        print(" 3) ACCOUNTANT")
        print(" 4) ML ENGINEER")
        print(" 5) PRINT ALLOCATED EMPLOYEES")
        print("-1) EXIT")
        option = int(input(" ENTER YOUR OPTION : ").strip())

        
        if option == -1:
            print("\n\n ***** EXIT *****")

        elif option ==5 :
            DisplayEmp()

        elif option in [1,2,3,4]:
            NO_CANDIDATE = 0
            print("\n\n **** ", post_list[option-1]," *****")

            while True:
                print("\n ENTER -1 TO END COST ANALYSIS")
                NO_CANDIDATE = int(input(" ENTER THE NUMBER OF CANDIDATES : ").strip())
                candidates = genrateList(NO_CANDIDATE)

                if NO_CANDIDATE <1:
                    print(" BEST EMPLOYEE ID FOR ",post_list[option-1] ," : ", BEST_INDEX[option-1] )
                    break

                scores = CalcScore(option-1 , candidates)
                hiring(scores, option-1)

        else:
            print("ENTER VALID OPTION!!"  )  



menu()


# LOGIC

# candidates = [

#     [10, 30, 3 ,49, 70, 78], <= skills
#     [],
#     []
#     .....

# ]


# SKILlS
#  0: HTML , 1: ENGLISH , 2: EXCEL, 3: PYTHON , 4: TAXATION , 5: AGILE 

# POSTS
# 0 -> WEB DEV , 1-> MANAGER , 2-> ACCOUNTANT , 3 -> ML 

# metrics = [
#     [0.6 , 0.05,  0.05 , 0.3 ,0 , 0.3] <= WEB DEV
#     [0.1, 0.4, 0.2, 0.05, 0.1, 0.4 ] <= MANAGER
#     [0, 0.4, 0.2, 0.05, 0.1, 0.4 ] <= ACCOUNTANT
#     [0.1, 0.1, 0.1, 0.6, 0, 0.2 ] <= ML

# ]