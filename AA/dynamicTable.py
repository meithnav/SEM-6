# DYNAMIC TABLE


def potential(N ,cost, table_size):
    print("\n\n*** POTENTIAL ***")
    pot_cost=[0]
    print("\nN\tCAPACITY\tACTUAL COST\tPOTENTIAL")
    for i in range(1, N):
        pot_cost.append(2*i - table_size[i-1])
        print(i, "\t     ",table_size[i-1],"\t   ", cost[i-1],"\t     ","\t",pot_cost[i])

 
    total_potential_cost=0
    for i in range(1, N-1):
        total_potential_cost += (cost[i] + pot_cost[i] - pot_cost[i-1])

    print("\n\nTOTAL COST : ", total_potential_cost)
    print("POTENTIAL COST PER STEP : ", total_potential_cost//N)


def accounting(cost):
    bank =0
    c_prime = 2
    print("\n\n*** ACCOUNTING ***")
    print("\nN\tACTUAL COST\tESTIMATED COST\tBANK")
    for i in range(0, len(cost)):
        bank += c_prime - cost[i]
        if bank<0:
            while bank<0:
                c_prime+=1
                bank+= (i)
        
        print(i+1, "\t     ", cost[i],"\t     ",c_prime,"\t",bank)
    print("\n\n ESTIMATED COST PER OPERATION : ", c_prime)
    

def dynamictable():
    N = 10
    CAPACITY = 1
    COST_PER_OPER = 1
    TOTAL_COST = 0
    cost_doubling = 0
    cost_arr =[]
    table_size =[]

    print("N\tCAPACITY\tCOST DOUBLING\tTOTAL COST")
    for i in range(1, N):

        if i ==1 :
            # EMPTY
            CAPACITY=1
            cost_doubling = 0

        else:
            if i>CAPACITY:
                # OVERFLOW
                cost_doubling = CAPACITY
                CAPACITY *=2
            else:
                cost_doubling = 0
        
        COST = cost_doubling + COST_PER_OPER
        cost_arr.append(COST)
        TOTAL_COST += COST
        table_size.append(CAPACITY)

        print(i,"\t     ",CAPACITY,"\t     ",cost_doubling,"\t    ",COST)


    # AGGREGATE
    print("\n\n*** AGGREGATE COST ***")
    print("ESTIMATED COST 3(N): ", 3*(N-1))
    print("REAL COST : ", TOTAL_COST)
    print("AGGREGATE COST PER OPERATION : ", TOTAL_COST//(N-1))

    accounting(cost_arr)
    potential(N, cost_arr , table_size)


dynamictable()             


