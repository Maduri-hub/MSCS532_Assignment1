def insertion_sort_descending(data):
    for index in range(1, len(data)):
        value = data[index]
        position = index - 1
        # Shift the numbers until this one is in the right place
        while position >= 0 and data[position] < value:
            data[position + 1] = data[position]
            position -= 1
        data[position + 1] = value
    return data


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    sorted_numbers = insertion_sort_descending(numbers)
    print("Sorted list in decreasing order:", sorted_numbers)
