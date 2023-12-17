# Josh Silva
# Sorting algos

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

def plot_step(arr, rects, title, text):
    for rect, val in zip(rects, arr):
        rect.set_height(val)
    text.set_text(title)

def selection(input_arr, rects, text):
    for i in range(len(input_arr)):
        min_val = i
        for j in range(i+1, len(input_arr)):
            if input_arr[min_val] > input_arr[j]:
                min_val = j
        input_arr[i], input_arr[min_val] = input_arr[min_val], input_arr[i]
        yield (input_arr, f'Selection Sort - Step {i * len(input_arr) + j}')

def bubble(input_arr, rects, text):
    for n in range(len(input_arr) - 1, 0, -1):
        for i in range(n):
            if input_arr[i] > input_arr[i + 1]:
                input_arr[i], input_arr[i + 1] = input_arr[i + 1], input_arr[i]
                yield(input_arr, f'Bubble Sort - Step {n*len(input_arr) + i}')

def insertion(input_arr, rects, text):
    for i in range(1, len(input_arr)):
        key = input_arr[i]
        j = i - 1
        while j >=0 and key < input_arr[j]:
            input_arr[j + 1] = input_arr[j]
            j -= 1
            yield (input_arr, f'Insertion Sort - Move element at index {i}')
        input_arr[j + 1] = key
        yield (input_arr, f'Insertion Sort - Place key at index {j+1}')

def merge(input_arr, start, end, rects, text):
    if end - start > 1:
        mid = (start + end) // 2

        yield from merge(input_arr, start, mid, rects, text)
        yield from merge(input_arr, mid, end, rects, text)

        merged = []
        left, right = start, mid
        while left < mid and right < end:
            if input_arr[left] < input_arr[right]:
                merged.append(input_arr[left])
                left += 1
            else:
                merged.append(input_arr[right])
                right += 1
        merged.extend(input_arr[left:mid])
        merged.extend(input_arr[right:end])

        for i, val in enumerate(merged):
            input_arr[start + i] = val
            yield (input_arr, f'Merge Sort - Merging {start} to {end}')

def merge_sort(input_arr, rects, text):
    yield from merge(input_arr, 0, len(input_arr), rects, text)

def quick(input_arr, low, high, rects, text):
    size = high - low + 1
    stack = [0] * (size)
    
    top = -1
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high
    
    while top >= 0:
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
        p = partition(input_arr, low, high)
        yield (input_arr, f'Quicksort - Pivot {input_arr[p]} at position {p}')
        if p - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1
        if p + 1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def animate(input_arr, sorting_algorithm, sort_method):
    fig, ax = plt.subplots()
    ax.set_title("Sorting Visualization")
    rects = ax.bar(range(len(input_arr)), input_arr, align="edge")
    text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

    def update(data):
        arr, title = data
        plot_step(arr, rects, title, text)

    save_count_estimate = len(input_arr) ** 2

    array_size = len(input_arr)
    if array_size <= 20:
        animation_interval = 100
    elif array_size <= 50:
        animation_interval = 50
    elif array_size <= 100:
        animation_interval = 20
    elif array_size <= 500:
        animation_interval = 10
    else:
        animation_interval = 5

    if sort_method == 5:
        frames = sorting_algorithm(input_arr, 0, len(input_arr) - 1, rects, text)
    else:
        frames = sorting_algorithm(input_arr, rects, text)

    ani = FuncAnimation(fig, func=update, frames=frames, repeat=False, blit=False, save_count=save_count_estimate, interval=animation_interval)
    plt.show()

method = {
    1: selection,
    2: bubble,
    3: insertion,
    4: merge_sort,
    5: quick
}

    
while True:
    try:
        size = int(input("Enter size of random array to generate (or 0 to quit): "))
        if size == 0:
            print("Program terminated.")
            break
        input_arr = [random.randint(1, 5000) for _ in range(size)]
        sort_method = int(input("Enter the number for the sort method to use: (1:selection, 2:bubble, 3:insertion, 4:merge, 5:quick): "))
        if sort_method in method:
            animate(input_arr, method[sort_method], sort_method)
        else:
            print("\nPlease enter a valid integer to identify a sort method\n")
            
    except ValueError:
        print("\nInvalid input. Please enter a valid integer.\n")
