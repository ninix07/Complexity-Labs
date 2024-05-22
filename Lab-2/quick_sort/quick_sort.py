def partition(Arr:list, start_index, end_index):
    x=Arr[end_index]
    i=start_index-1
    for j  in range (start_index , end_index):
        if Arr[j] <= x:
            i= i+1
            Arr[i], Arr[j]= Arr[j], Arr[i]
    Arr[i+1], Arr[end_index]= Arr[end_index], Arr[i+1]
    return i+1

def quick_sort(Arr:list, start_index, end_index):
    if start_index < end_index:
        mid_index= partition(Arr, start_index, end_index)
        quick_sort(Arr, start_index, mid_index-1)
        quick_sort(Arr, mid_index+1, end_index)
    return Arr

if __name__ == "__main__":
    A= quick_sort([2,4,7,8,3,1],0,5)
    print(A)