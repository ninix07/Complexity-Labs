def counting_sort(A,max):
    size= len(A)
    C=[0 for i in range(max+1)]       # make a new array for count of the elements
    B=[0 for i in range(size)]        #make a new sorted array
    for j in range( size):            # if A[j]=1 then updating C[1]= 0+1= 1 
        C[A[j]]=C[A[j]]+1
    for i in range(1,max+1):          # accumulating the count 
        C[i]=C[i]+C[i-1]              #using 1 in range to avoid adding -1 index in first
    print(C)
    for j in range(size-1,-1,-1):      # now putting value in array B 
        B[C[A[j]]-1]=A[j]
        C[A[j]]=C[A[j]]-1
    return B

def counting_sort_radix(A,main):
    size= len(A)
    max= 0
    for i in range(size):
        if A[i]> max:
            max= A[i]
    print(max)
    C=[0 for i in range(max+1)]       # make a new array for count of the elements
    B=[0 for i in range(size)]        #make a new sorted array
    for j in range( size):            # if A[j]=1 then updating C[1]= 0+1= 1 
        C[A[j]]=C[A[j]]+1
    for i in range(1,max+1):          # accumulating the count 
        C[i]=C[i]+C[i-1]              #using 1 in range to avoid adding -1 index in first
    for j in range(size-1,-1,-1):      # now putting value in array B 
        B[C[A[j]]-1]=main[j]
        C[A[j]]=C[A[j]]-1
    return B

def radix_sort(A):
    curr_place=[]
    divisor= 1
    for i in range(3):
        for element in A:
            value= (element//divisor)%10
            curr_place.append(value)
        A=counting_sort_radix(curr_place,A)
        divisor= divisor*10
        curr_place.clear()
    return A
        
        
if __name__=="__main__":
    A=[200,801,507,302,901,402,111]
    sorted= radix_sort(A)
    print(sorted)