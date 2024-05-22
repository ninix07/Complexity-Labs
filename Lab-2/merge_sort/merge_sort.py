import math
import sys
def Merge(Arr: list, start_index: int,mid_index:int, end_index:int):
    n1= mid_index-start_index+1
    n2= end_index-mid_index
    L= [0 for i in range(n1+1)]
    R=[0 for i in range(n2+1)]
    for i in range(n1):
        L[i]= Arr[start_index+i]
    for j in range(n2):
        R[j]= Arr[mid_index+j+1]
    inf= sys.maxsize
    L[n1]= inf
    R[n2]= inf
    i,j=0,0
    for k in range (start_index, end_index+1):
        if L[i]<= R[j]:
            Arr[k]=L[i]
            i=i+1
        else:
            Arr[k]=R[j]
            j=j+1
        
    
def merge_sort(Arr: list, start_index: int, end_index:int ):
    if start_index < end_index:
        mid_index= math.floor((start_index+end_index)/2.0)
        merge_sort(Arr,start_index,mid_index)
        merge_sort(Arr, mid_index+1, end_index)
        Merge(Arr, start_index,mid_index,end_index)

    return Arr  

        
if __name__ == "__main__":
    A= merge_sort([2,4,7,8,3,1],0,5)
    print(A)