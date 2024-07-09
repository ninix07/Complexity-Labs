def max_heapify(A, i, size):
    left = 2 * i + 1                           #defne right child of the node
    right = 2 * i + 2                          #defiune left child of node
    largest = i                                 #let current node is largest            
    if left < size and A[left] > A[largest]:      #check if left child largest
        largest = left
    if right < size and A[right] > A[largest]:   #check if right child largest
        largest = right
    if largest != i:                             #if current node is not largest then swap the largest and current element and again reheapify
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, size)

def build_max_heap(A, size):                       #build heap in  the beginning
    for i in range(size // 2 - 1, -1, -1):
        max_heapify(A, i, size)

def heapSort(A):                           
    size = len(A)                     
    build_max_heap(A, size)                  
    for i in range(size - 1, 0, -1):
        A[0], A[i] = A[i], A[0]                        #since the largest element is being found first it is sent back to ith index for sorting
        max_heapify(A, 0, i)


if __name__=="__main__":
    A=[2,8,5,3,9,4,1]
    heapSort(A)
    print(A)