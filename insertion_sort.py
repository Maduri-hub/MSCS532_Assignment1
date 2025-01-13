def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    numbers = [12, 11, 13, 5, 6]
    print("Original list:", numbers)
    sorted_numbers = insertion_sort_descending(numbers)
    print("Sorted list in decreasing order:", sorted_numbers)
