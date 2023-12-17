# Josh Silva
# Sorting algos
import random


def selection(input_arr):
    for i in range(len(input_arr)):
        min_val = i
        for j in range(i+1, len(input_arr)):
            if input_arr[min_val] > input_arr[j]:
                min_val = j
        input_arr[i], input_arr[min_val] = input_arr[min_val], input_arr[i]
    return input_arr

def bubble(input_arr):
    for n in range(len(input_arr) - 1, 0, -1):
        for i in range(n):
            if input_arr[i] > input_arr[i + 1]:
                input_arr[i], input_arr[i + 1] = input_arr[i + 1], input_arr[i]
    return input_arr

def insertion(input_arr):
    for i in range(1, len(input_arr)):
        key = input_arr[i]
        j = i - 1
        while j >=0 and key < input_arr[j]:
            input_arr[j + 1] = input_arr[j]
            j -= 1
        input_arr[j + 1] = key
    return input_arr

def merge(input_arr):
    if len(input_arr) > 1:
        mid = len(input_arr) // 2
        L = input_arr[:mid]
        R = input_arr[mid:]

        merge(L)
        merge(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                input_arr[k] = L[i]
                i += 1
            else:
                input_arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            input_arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            input_arr[k] = R[j]
            j += 1
            k += 1
    return input_arr

def quick(input_arr):
    if len(input_arr) <= 1:
        return input_arr
    else:
        pivot = input_arr[0]
        less = [x for x in input_arr[1:] if x <= pivot]
        greater = [x for x in input_arr[1:] if x > pivot]
        return quick(less) + [pivot] + quick(greater)

method = {
    1: selection,
    2: bubble,
    3: insertion,
    4: merge,
    5: quick
}
    
while True:
    try:
        size = int(input("Enter size of random array to generate (or 0 to quit): "))
        if size == 0:
            print("Program terminated.")
            break
        input_arr = [random.randint(1, 5000) for _ in range(size)]
        print("Randomly generated array:\n", input_arr, "\n")

        sort_method = int(input("Enter the number for the sort method to use: (1:selection, 2:bubble, 3:insertion, 4:merge, 5:quick): "))
        if sort_method in method:
            print("Sorted array:\n", method[sort_method](input_arr), "\n")
        else:
            print("\nPlease enter a valid integer to identify a sort method\n")
            
    except ValueError:
        print("\nInvalid input. Please enter a valid integer.\n")
