def Partition(A,high,low):
    x=A[high]
    i=low -1
    for j in range (low,high):
        if A[j] <= x:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[high]= A[high],A[i+1]
    return i+1


def quick_sort(A,high,low):
    if low <high:
        mid= Partition(A,high,low)
        quick_sort(A,mid-1,low)
        quick_sort(A,high, mid+1)
    return A
if __name__=="__main__":
    A=[2,8,5,3,9,4,1]
    sorted=quick_sort(A,len(A)-1,0)
    print(sorted)