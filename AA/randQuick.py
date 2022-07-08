import time
import random


def generateNum(N):
    arr=[]
    for i in range(N):
        arr.append(random.randint(0, 10000))

    return arr


def swap(A, i, j):
    A[i] , A[j] = A[j], A[i]


def randomiseArr(arr):

    # METHOD 1:
    # random.shuffle(arr)

    # METHOD 2:
    for i in range(len(arr)-1 , 0 , -1):
        j = random.randint(0, i-1) 
        swap(arr , i,j)

    # print("AFTER SHUFFLE : ", arr)
    return arr


def HoarePartition(array, low, high) -> int:
    pivot = array[low]
    i, j = (low - 1, high + 1)
 
    while True:
 
        while True:
            i = i + 1
            if array[i] >= pivot:
                break
 
        while True:
            j = j - 1
            if array[j] <= pivot:
                break
 
        if i >= j:
            return j
 
        swap(array, i, j)


def HoareQuicksort(array, low, high):
    if low < high:
        pivot = HoarePartition(array, low, high)
        HoareQuicksort(array, low, pivot)
        HoareQuicksort(array, pivot + 1, high)
    return array


def Lumotopartition(array, lo, hi):
    pivot = array[hi]

    i = lo - 1 # SMALLER ELEM POINTER
    for j in range(lo, hi): # LOOP POINTER
        if array[j] < pivot:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp


    # SWAP PIVOT
    temp = array[i + 1]
    array[i + 1] = array[hi]
    array[hi] = temp
    return i + 1


def LumotoQuicksort(array, lo, hi):
    if lo < hi:
        p = Lumotopartition(array, lo, hi)
        LumotoQuicksort(array, lo, p - 1)
        LumotoQuicksort(array, p + 1, hi)
    return array


def baseQuicksort(array, lo, hi):
    if lo < hi:
        p =lo+1
        baseQuicksort(array, lo, p - 1)
        baseQuicksort(array, p + 1, hi)
    return array



def medianThreePartition(array, low , high) -> int:
    # print(array[low:high+1])
    if high-low+1>2:
        index = random.randint(low+1, high-1)
    else:
        return low

    if array[low]>array[high] and array[low]>array[index]:
        if array[index]>array[high]:
            return high
        else:
            return index
    
    elif array[index]>array[high] and array[index]>array[low]:
        if array[low]>array[high]:
            return high
        else:
            return low

    elif array[high]>array[index] and array[high]>array[low]:
        if array[index]>array[low]:
            return low
        else:
            return index
    

def medianQuicksort(array, lo, hi):
    if lo < hi:
        p = medianThreePartition(array, lo, hi)
        medianQuicksort(array, lo, p - 1)
        medianQuicksort(array, p + 1, hi)
    return array



def menu():
    option=0
    while(option != -1):

        print("\n **** MAIN MENU *****\n")
        print(" 1) QUICK SORT USING HOARE PARTITIONING")
        print(" 2) QUICK SORT USING LUMOTO PARTITIONING")
        print("-1) EXIT")
        option = int(input(" ENTER YOUR OPTION : ").strip())

        if option ==1:
            print("\n **** QUICK SORT USING HOARE PARTITIONING *****\n")
            ip_arr = list(map(int, input("ENTER THE LIST OF NUMBERS : ").split() ))
            arr = randomiseArr(ip_arr)            
            startHoare = time.perf_counter()
            print("SORTED ARRAY USING HOARE : {s} ".format( s= " ".join( str(ele) for ele in  HoareQuicksort(arr, 0, len(arr) - 1))))
            endHoare = time.perf_counter()
            print(f"TIME ELAPSED FOR HOARE : {endHoare - startHoare:0.9f} seconds")

        elif option ==2:
            print("\n **** QUICK SORT USING LUMOTO PARTITIONING *****\n")
            ip_arr = list(map(int, input("ENTER THE LIST OF NUMBERS : ").split() ))
            arr = randomiseArr(ip_arr)
            startLumoto = time.perf_counter()
            print("SORTED ARRAY USING LUMOTO : {s} ".format( s= " ".join( str(ele) for ele in  LumotoQuicksort(arr, 0, len(arr) - 1))))
            endLumoto = time.perf_counter()
            print(f"TIME ELAPSED FOR LUMOTO : {endLumoto - startLumoto:0.9f} seconds")

        
        elif option == -1:
            print("\n\n ***** EXIT *****")

        else:
            print("ENTER VALID OPTION!!"  )  



def quicksort():

    # menu()
    N = 500
    gen_arr = generateNum(N)
    arr = randomiseArr(gen_arr)
    # arr = list(map(int, input("ENTER THE LIST OF NUMBERS : ").split() ))


    print("\n NO. OF ELEMENTS : ", len(arr))
    
    print("\n **** SIMPLE QUICK SORT *****")
    startQuick = time.perf_counter()
    quick_arr = baseQuicksort(arr, 0, len(arr) - 1)
    endQuick = time.perf_counter()
    # print("CUSTOM SORTED : ", quick_arr)
    # print("SORTED ARRAY USING SIMPLE QUICKSORT : {s} ".format( s= " ".join( str(ele) for ele in  baseQuicksort(arr, 0, len(arr) - 1))))
    print(f"TIME ELAPSED FOR SIMPLE QUICKSORT : {endQuick - startQuick:0.9f} seconds")

    
    print("\n **** QUICK SORT USING HOARE PARTITIONING *****")
    startHoare = time.perf_counter()
    hoare_arr = HoareQuicksort(arr, 0, len(arr) - 1)
    endHoare = time.perf_counter()
    # print("HOARE SORTED : ", hoare_arr)
    # print("SORTED ARRAY USING HOARE : {s} ".format( s= " ".join( str(ele) for ele in  HoareQuicksort(arr, 0, len(arr) - 1))))
    print(f"TIME ELAPSED FOR HOARE : {endHoare - startHoare:0.9f} seconds")


    print("\n **** QUICK SORT USING LUMOTTO PARTITIONING *****")
    startLumoto = time.perf_counter()
    lumotto_arr  =LumotoQuicksort(arr, 0, len(arr) - 1)
    endLumoto = time.perf_counter()
    # print("LUMOTO SORTED : ", lumotto_arr)
    # print("SORTED ARRAY USING LUMOTO : {s} ".format( s= " ".join( str(ele) for ele in  LumotoQuicksort(arr, 0, len(arr) - 1))))
    print(f"TIME ELAPSED FOR LUMOTO : {endLumoto - startLumoto:0.9f} seconds")


    # print("\n **** QUICK SORT USING MEDIAN PARTITIONING *****")
    # startMedian = time.perf_counter()
    # median_arr = medianQuicksort(arr, 0, len(arr) - 1)
    # endMedian = time.perf_counter()
    # # print("MEDIAN SORTED : ", median_arr)
    # # print("SORTED ARRAY USING MEDIAN : {s} ".format( s= " ".join( str(ele) for ele in  medianQuicksort(arr, 0, len(arr) - 1))))
    # print(f"TIME ELAPSED FOR MEDIAN : {endMedian - startMedian:0.9f} seconds")
         


quicksort()



# 40 2 5 86 21 10 88 29 6 8 17 100 43 87 
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
# 10 10 10 10 10 10 10 10 10 10 10 10 10
# 10 20 15 19