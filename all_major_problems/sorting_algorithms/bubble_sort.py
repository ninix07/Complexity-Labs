def bubble_sort(A):
    size= len(A)
    for i in range(size):                    #outer loop for iterating through all elements
        for j in range(0,size-i-1):          #inner loop for only swapping between element that are not in the right sorted zone
            if A[j] > A[j+1]:                #swap when jth element is greater than in j+1th element
                A[j],A[j+1]=A[j+1],A[j]    
    return A

if __name__=="__main__":
    A=[2,8,5,3,9,4,1]
    sorted= bubble_sort(A)
    print(sorted)