import random
import time

# Deterministic partition (uses last element as pivot)
def deterministic_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Randomized partition (selects a random pivot)
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return deterministic_partition(arr, low, high)

# Deterministic Quicksort
def deterministic_quick_sort(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quick_sort(arr, low, pi - 1)
        deterministic_quick_sort(arr, pi + 1, high)

# Randomized Quicksort
def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)

def print_array(arr):
    print("[", end="")
    print(", ".join(map(str, arr)), end="")
    print("]")

if __name__ == "__main__":
    array_size = int(input("Enter the size of the array: "))
    arr = []
    for i in range(array_size):
        element = int(input(f"Enter the {i+1} element of the array: "))
        arr.append(element)

    print("Original array is:", end=" ")
    print_array(arr)

    while True:
        print('*' * 10, "MENU", '*' * 10)
        print("Choose the sorting method")
        print("1. Deterministic Quicksort")
        print("2. Randomized Quicksort")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            arr_deterministic = arr.copy()  # Create a copy for deterministic sort
            start_time = time.time()
            deterministic_quick_sort(arr_deterministic, 0, len(arr_deterministic) - 1)
            deterministic_time = time.time() - start_time
            print("\nSorted array using Deterministic Quicksort:", end=" ")
            print_array(arr_deterministic)
            print(f"Time taken by Deterministic Quicksort: {deterministic_time:.6f} seconds")

        elif choice == 2:
            arr_randomized = arr.copy()  # Create a copy for randomized sort
            start_time = time.time()
            randomized_quick_sort(arr_randomized, 0, len(arr_randomized) - 1)
            randomized_time = time.time() - start_time
            print("\nSorted array using Randomized Quicksort:", end=" ")
            print_array(arr_randomized)
            print(f"Time taken by Randomized Quicksort: {randomized_time:.6f} seconds")

        elif choice == 3:
            print("Exiting successfully!!")
            break

        else:
            print("Invalid choice!")
