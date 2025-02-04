import random
import timeit

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def tim_sort(arr):
    return sorted(arr)

def generate_random_list(size, min_val=0, max_val=10000):
    return [random.randint(min_val, max_val) for _ in range(size)]


def main():
    sizes = [100, 1000, 5000, 10000]
    for size in sizes:
        data = generate_random_list(size)
        print(f"\nArray size: {size}")
        
        insertion_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
        print(f"Insertion Sort: {insertion_time:.6f} sec")
        
        merge_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
        print(f"Merge Sort: {merge_time:.6f} sec")
        
        timsort_time = timeit.timeit(lambda: tim_sort(data.copy()), number=1)
        print(f"Timsort (Python sorted): {timsort_time:.6f} sec")



if __name__ == "__main__":
    main()
