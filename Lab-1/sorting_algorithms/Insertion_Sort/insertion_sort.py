def insertion_sort(A):
    n=len(A)
    for  i in range(1, n):
        value = A[i]
        j= i-1
        while j >= 0 and value < A[j]:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=value       
    return A

if __name__ == "__main__":
    A= insertion_sort([2,4,7,8,3,1])
    print(A)

    