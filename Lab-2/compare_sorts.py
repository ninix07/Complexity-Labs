from merge_sort.merge_sort import merge_sort
from quick_sort.quick_sort import quick_sort
from insertion_sort.insertion_sort import insertion_sort
from selection_sort.selection_sort import selectionSort
import time
import random
from datetime import datetime
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(200000)
def quick_sort_best_case_arr(
    arr, start_index: int = 0, end_index: int | None = None
):


    if end_index is None:
        end_index = len(arr) - 1

    if start_index >= end_index:
        return

    if (start_index == 0) and (end_index == (len(arr) - 1)):  # only sorting once
        arr.sort()

    median = (start_index + end_index) // 2

    i = median
    # move the median to last index
    while i < end_index:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i += 1

    quick_sort_best_case_arr(arr, start_index, median - 1)
    quick_sort_best_case_arr(arr, median, end_index - 1)
    return arr

def worst_case_merge_arr(arr,sort=True):
    n = len(arr)
    if n <= 1:
        return arr

    if n == 2:
        arr[0], arr[1] = arr[1], arr[0]
        return arr
    if sort:
        arr = sorted(arr)
    else:
        arr = arr.copy()
    left_arr = arr[::2]
    right_arr = arr[1::2]
    return worst_case_merge_arr(left_arr,sort=False) + worst_case_merge_arr(right_arr,sort=False)
def compare_sorts():
    step_size = 1000
    max_size = 11000
    curr_size = 1000

    size = []
    quick_time = []
    merge_time = []
    quick_worst_time = []
    quick_sort_best_time=[]
    merge_best_time=[]
    merge_worst_time=[]
    insertion_time=[]
    selection_time=[]
    for _ in range(14):
        random.seed(datetime.now().timestamp())
        A = [random.randint(0, 10000) for _ in range(curr_size)]
        B = A.copy()
        C=A.copy()
        D=A.copy()
        size.append(curr_size)
        curr_size += step_size

        # Measure merge sort time
        merge_sort_start_time = time.time()
        merge_sort(B, 0, len(B) - 1)
        merge_sort_end_time = time.time()
        #merge_best_time(when sorted)
        merge_sort_best_start_time = time.time()
        merge_sort(B, 0, len(B) - 1)
        merge_sort_best_end_time = time.time()
        #merge_worst_time
        B= worst_case_merge_arr(B)
        merge_sort_worst_start_time = time.time()
        merge_sort(B, 0, len(B) - 1)
        merge_sort_worst_end_time = time.time()
        # Measure quick sort time
        quick_sort_start_time = time.time()
        quick_sort(A, 0, len(A) - 1)
        quick_sort_end_time = time.time()

        # Measure worst-case quick sort time (sorted array)
        quick_sort_worst_start_time = time.time()
        quick_sort(A, 0, len(A) - 1)
        quick_sort_worst_end_time = time.time()

        #Measure quick sort best case (median as pivot element)
        A=quick_sort_best_case_arr(A)
        quick_sort_best_start_time=time.time()
        quick_sort(A, 0, len(A) - 1)
        quick_sort_best_end_time=time.time()
        #selection and insertion sort for same data
        selection_sort_start_time=time.time()
        selectionSort(C)
        selection_sort_end_time=time.time()
        insertion_sort_start_time=time.time()
        insertion_sort(D)
        insertion_sort_end_time=time.time()
        # Calculate times in milliseconds
        total_quick_time = (quick_sort_end_time - quick_sort_start_time) * 1000
        total_merge_time = (merge_sort_end_time - merge_sort_start_time) * 1000
        total_quick_worst_time = (quick_sort_worst_end_time - quick_sort_worst_start_time) * 1000
        total_quick_best_time = (quick_sort_best_end_time - quick_sort_best_start_time) * 1000
        total_merge_best_time = (merge_sort_best_end_time - merge_sort_best_start_time) * 1000
        total_merge_worst_time = (merge_sort_worst_end_time - merge_sort_worst_start_time) * 1000
        total_insertion_time= (insertion_sort_end_time-insertion_sort_start_time)*1000
        total_selection_time= (selection_sort_end_time- selection_sort_start_time)*1000
      
        # Append data for plotting
        quick_time.append(total_quick_time)
        merge_time.append(total_merge_time)
        quick_worst_time.append(total_quick_worst_time)
        quick_sort_best_time.append(total_quick_best_time)
        merge_best_time.append(total_merge_best_time)
        merge_worst_time.append(total_merge_worst_time)
        insertion_time.append(total_insertion_time)
        selection_time.append(total_selection_time)

    # Create figure and subplots
    fig, axs = plt.subplots(4, 1, figsize=(10, 15))
    #For quick and merge
    # Plot average case
    axs[0].plot(size, quick_time, label="Quick Sort")
    axs[0].plot(size, merge_time, label="Merge Sort")
    axs[0].legend(loc='upper left')
    axs[0].set_xlabel("Array Size")
    axs[0].set_ylabel("Time Taken (ms)")
    axs[0].set_title("Average Case")

    # Plot worst case
    axs[1].plot(size, merge_worst_time, label="Merge Sort (Worst Case)")
    axs[1].plot(size, quick_worst_time, label="Quick Sort (Worst Case)")
    axs[1].legend(loc='upper left')
    axs[1].set_xlabel("Array Size")
    axs[1].set_ylabel("Time Taken (ms)")
    axs[1].set_title("Worst Case")

    # Plot best case
    axs[2].plot(size, merge_best_time, label="Merge Sort (Best Case)")
    axs[2].plot(size, quick_sort_best_time, label="Quick Sort (Best Case)")
    axs[2].legend(loc='upper left')
    axs[2].set_xlabel("Array Size")
    axs[2].set_ylabel("Time Taken (ms)")
    axs[2].set_title("Best Case")
    # Plot other sorts 
    axs[3].plot(size, insertion_time, label="Insertion Sort")
    axs[3].plot(size, selection_time, label="Selection Sort")
    axs[3].legend(loc='upper left')
    axs[3].set_xlabel("Array Size")
    axs[3].set_ylabel("Time Taken (ms)")
    axs[3].set_title("Insertion and Selection Sort")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
   compare_sorts()