def bubble_sort(arr):
    n = len(arr)
    sorted_arr = arr.copy()

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        if not swapped:
            break

    return sorted_arr


def extract_unique_letters(name):
    unique_letters = []
    for char in name.upper():
        if char.isalpha() and char not in unique_letters:
            unique_letters.append(char)
    return unique_letters


def main():
    full_name = "JAMES RYAN R. MARTINEZ"

    unsorted_array = extract_unique_letters(full_name)

    sorted_array = bubble_sort(unsorted_array)

    print("Full Name:      ", full_name)
    print("Unsorted Array: ", unsorted_array)
    print("Sorted Array:   ", sorted_array)


if __name__ == "__main__":
    main()