import random
import time

# Deterministic Quick Sort
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return deterministic_quick_sort(less) + [pivot] + deterministic_quick_sort(greater)

# Randomized Quick Sort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return randomized_quick_sort(less) + equal + randomized_quick_sort(greater)

# Function to analyze sorting time
def analyze_sorting_time(sorting_function, arr):
    start_time = time.time()
    sorting_function(arr)
    end_time = time.time()
    return end_time - start_time

# Generate a random list of numbers for sorting
arr = random.sample(range(1, 1000), 100)

# Analyze and compare the sorting time for deterministic and randomized Quick Sort
deterministic_time = analyze_sorting_time(deterministic_quick_sort, arr.copy())
randomized_time = analyze_sorting_time(randomized_quick_sort, arr.copy())

print(arr)
print("Deterministic Quick Sort time:", deterministic_time)
print("Randomized Quick Sort time:", randomized_time)
