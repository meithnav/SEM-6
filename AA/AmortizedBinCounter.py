
import itertools

def BinaryCounter(n, COUNTS):
    counter=[]
    for i in itertools.product([0,1],repeat=n): 
        counter.append(list(i))

    # for arr in counter[:COUNTS+1]:
    #     print(arr)

    return counter[:COUNTS+1]

def getPotential(counter, cur, prev):
    x=0
    t=0

    if prev ==-1:
        return 1,0

    for i in range(len(counter[cur])):
        if counter[cur][i] != counter[prev][i]:
            x+=1
        if counter[cur][i]==1  and counter[prev][i]==0:
            t+=1

    return x,t


def costList(counter, K_BITS):
    flips=[0]
    pot =[(0,0)]

    for i in range(1, len(counter)):
        flip=0
        pot.append(getPotential(counter, i-1 , i-2) )
        for j in range(K_BITS):
            if counter[i-1][j] != counter[i][j]:
                flip+=1

        flips.append(flip)

    # print("FLIPS : ", flips, "LEN : ", len(flips))
    return flips , pot


def printTable(actualCost, pot ,COUNTS):
    print("\nITER\tACTUAL COST\tPOTENTAIL")
    # print('-'*5,'\t','-'*15, '\t', '-'*5, '\t','-'*5)
    print('-'*34)

    for i in range(0, COUNTS+1):
        print(i,"\t    ", actualCost[i],"\t\t   ", pot[i][0])


def Aggregate(actualCost,COUNTS):
    print("\n\n****** AGGREGATE ANALYSIS *******\n")

    total=0
    print("COUNT\tNO. OF FLIPS")
    print('-'*20)
    for i in range(len(actualCost)):
        print(" ",i,"\t    ",actualCost[i])
        total += actualCost[i]

    print("\n CALCULATED AGGREGATE TOTAL COST : ", total)
    print(" IDEAL TOTAL COST (2n) : ", 2*COUNTS)
    # print("AGGREGATE COST : {:.2f} ".format(total/COUNTS) )
    print(" OVERALL AGGREGATE COST PER OPERATION : {} ".format(total//(COUNTS-1)) )


    # return total/COUNTS

def Potential(counter , actualCost, pot , COUNTS):
    print("\n\n****** POTENTIAL ANALYSIS *******\n")
    printTable(actualCost, pot ,COUNTS)
    total= 0
    cost_per_step=1
    for i in range(1, COUNTS+1):
        x_prev, t_prev= getPotential(counter, i-1 , i-2)
        x_cur, t_cur = getPotential(counter,i , i-1)
        total += (t_cur + cost_per_step) +(x_prev-t_prev+1)-(x_prev-t_prev+1)
    
    
    print(" CALCULATED TOTAL COST : ",total)
    print(" COST PER STEP : ",total//COUNTS)



def Accounting(counter , actualCost, K_BITS , COUNTS):
    estimated_cost = 1
    bank=0
    print("\n****** ACCOUNTING ANALYSIS *******")
    print("\nITER\tACTUAL COST\tESTIMATED COST\tBANK")
    # print('-'*5,'\t','-'*15, '\t', '-'*5, '\t','-'*5)
    print('-'*44)

    for i in range(0, COUNTS+1):
        print(i,"\t    ", actualCost[i],"\t\t    ", estimated_cost, "\t\t", bank)

        bank += estimated_cost-actualCost[i]
        if bank<0:
            # INCREMENT ESTIMATION TO MAKE BANK POSITIVE
            while bank<0:
                estimated_cost += 1
                bank += i


    print("\n ACCOUNTING COST PER OPERATION : ", estimated_cost)

    

def main():
    K_BITS =7
    COUNTS=17
    counter = BinaryCounter(K_BITS , COUNTS)
    actualCost , pot = costList(counter , K_BITS)
    Accounting(counter, actualCost,K_BITS , COUNTS)
    Aggregate(actualCost,COUNTS)
    Potential(counter,actualCost, pot, COUNTS)
    print("\n\n***** EXIT *****")

main()


