def selection_sort(A):
    size= len(A)
    for i in range(0,size):
        min_index= i                    #primarily stores ith index as min index
        for j in range(i+1,size):
            if A[j] < A[min_index]:   # if any element is smaller than the minimum index element then it is new min index
                min_index = j
        A[min_index],A[i]=A[i],A[min_index] #swap ith element with minimum index element
    return A


if __name__=="__main__":
    A=[2,8,5,3,9,4,1]
    sorted= selection_sort(A)
    print(sorted)