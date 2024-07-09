import sys
def merge(A,high,low, mid):
    n1= mid-low+1
    n2 =high-mid
    L= [A[low+i] for i in range(n1)]
    R=[A[mid+1+j] for j in range(n2)]
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i,j = 0,0
    for k in range(low,high+1):
        if L[i] <= R[j]:
            A[k]= L[i]
            i=i+1
        else:
           A[k]= R[j]
           j=j+1 
def merge_sort(A,low,high):
    if low < high:
        mid= (low+high)//2
        merge_sort(A,low,mid)
        merge_sort(A,mid+1,high)
        merge(A,high,low,mid)
    return A
    
if __name__=="__main__":
    A=[2,8,5,3,9,4,1]
    sorted=merge_sort(A,0,len(A)-1)
    print(sorted)