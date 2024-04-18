from Insertion_Sort.insertion_sort import insertion_sort
from Selection_sort.selection_sort import selectionSort
import time
import csv
import random
from datetime import datetime
import matplotlib.pyplot as plt
def compare_sorts():
    size=[]
    insertion_time=[]
    insertion_best_time=[]
    insertion_worst_time=[]
    selection_time=[]
    step_size= 10
    curr_size=1000
    for i in  range(1000):
        A=[]
        random.seed(datetime.now().timestamp())
        A = [random.randint(0, 10000) for _ in range(curr_size)]
        size.append(curr_size)
        curr_size+=step_size
        B=A.copy()
        selection_sort_start_time=time.time()
        selectionSort(B)
        selection_sort_end_time=time.time()
        insertion_sort_start_time=time.time()
        insertion_sort(A)
        insertion_sort_end_time=time.time()
        insertion_sort_best_start_time=time.time()
        insertion_sort(A)
        insertion_sort_best_end_time=time.time()
        A.sort(reverse=True)
        insertion_sort_worst_start_time=time.time()
        insertion_sort(A)
        insertion_sort_worst_end_time=time.time()
       
        total_insertion_time= (insertion_sort_end_time-insertion_sort_start_time)*1000
        total_insertion_best_time= (insertion_sort_best_end_time-insertion_sort_best_start_time)*1000
        total_insertion_worst_time= (insertion_sort_worst_end_time-insertion_sort_worst_start_time)*1000
        total_selection_time= (selection_sort_end_time- selection_sort_start_time)*1000
        insertion_time.append(total_insertion_time)
        insertion_best_time.append(total_insertion_best_time)
        insertion_worst_time.append(total_insertion_worst_time)
        selection_time.append(total_selection_time)
        data= ( len(B),total_insertion_time, total_selection_time,total_insertion_best_time, total_insertion_worst_time)
        with open('comapre_sorts.csv', 'a', newline='') as csvfile:
            writer =csv.writer(csvfile, delimiter=",")
            writer.writerow(data)
    fig, ax = plt.subplots()
    ax.plot(size, insertion_time , label="Insertion Sort")
    ax.plot(size, selection_time,label="Selection Sort")
    ax.plot(size, insertion_best_time, label="Insertion Sort(Best Case)")
    ax.plot(size,insertion_worst_time,label="Insertion Sort(Worst Case)")
    ax.xlabel("Array Size")
    ax.ylabel('Time Taken(seconds)')
    plt.show()

if __name__== "__main__":
    compare_sorts()