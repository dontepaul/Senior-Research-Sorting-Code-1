import random
import time

# Bubble Sort Function
def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Quick Sort Function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    less = [elem for elem in arr if elem < pivot]
    equal = [elem for elem in arr if elem == pivot]
    greater = [elem for elem in arr if elem > pivot]

    return quick_sort(less) + equal + quick_sort(greater)

# Generate random array
arr_length = 10000 #Change as need be for array size
random_arr = [random.randint(0, 99) for _ in range(arr_length)]

# Make a copy for each sorting algorithm
arr1 = random_arr.copy()
arr2 = random_arr.copy()

# Time Bubble Sort
start = time.time()
bubble_sort(arr1)
bubble_duration = time.time() - start

# Time Quick Sort
start = time.time()
sorted_arr = quick_sort(arr2)
quick_duration = time.time() - start

# Print results
print("Original array:", random_arr)
print("Sorted array using Bubble Sort:", arr1)
print("Sorted array using Quick Sort:", sorted_arr)

print(f"\n {bubble_duration:.5f} ")
print(f"{quick_duration:.5f} ")

