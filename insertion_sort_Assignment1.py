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
    elements = [45, 23, 89, 7, 12]
    print("Original list:", elements)
    sorted_elements = insertion_sort_descending(elements)
    print("Sorted list in decreasing order:", sorted_elements)