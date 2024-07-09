def insertion_sort(A):
    size= len(A)
    for j in range(1,size):
        key= A[j]                           #current element as key
        i=j-1                               # initilaizing sorted partition index end to be just below current index
        while i >=0 and key< A[i]:          #iterating through partition index until we find the right place
            A[i+1]=A[i]                     #moving the partition element by one place if it is greater than key element
            i-=1
        A[i+1]=key                          #putting key in right place
    return A
            

if __name__=="__main__":
    A=[2,8,5,3,9,4,1]
    sorted= insertion_sort(A)
    print(sorted)