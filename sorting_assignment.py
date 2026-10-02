"""Implementations for the Sorting Assignment exercises.

Algorithms that sort an input continue to sort it in place. Exercise functions
retain their original demonstration-oriented print behavior; the notebook keeps
sample data and invocations separate from these implementations.
"""


def selection_sort(arr):
    """Sort ``arr`` in place using selection sort."""
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[minimum] > arr[j]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
    return arr


def maximum(arr):
    """Print the sorted input and its most frequent value."""
    selection_sort(arr)
    print(arr)
    count = 1
    result = arr[0]
    max_count = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
            result = arr[i - 1]
    print(f"Value appearing maximum number of time in given array is -> {result}")


def missing_element(arr):
    """Print the missing value from the 1..n sequence represented by arr."""
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    missing_number = expected_sum - sum(arr)
    print(f"Missing number is -> {missing_number}")


def odd_time(arr):
    """Print the value whose occurrences have odd parity, using XOR."""
    result = 0
    for element in arr:
        result ^= element
    print(f"{result} occurs odd times")


def bubble_sort(arr):
    """Sort ``arr`` in place using the shared bubble-sort implementation."""
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def sum1(arr, k):
    """Print a pair summing to k, after sorting and printing arr."""
    bubble_sort(arr)
    print(arr)
    left = 0
    right = len(arr) - 1
    found = False
    while left < right:
        pair_sum = arr[left] + arr[right]
        if pair_sum == k:
            print(f"Two elements are {arr[left]}, {arr[right]}")
            found = True
            break
        elif pair_sum > k:
            right -= 1
        else:
            left += 1
    if not found:
        print(f"No elements sum matching give number -> {k}")


def sum_close_to_zero(arr):
    """Print the pair selected by the original two-pointer exercise."""
    bubble_sort(arr)
    print(arr)
    left = 0
    right = len(arr) - 1
    min_left = left
    min_right = right
    min_sum = arr[left] + arr[right]
    min_abs_sum = abs(min_sum)
    while left < right:
        current_sum = arr[left] + arr[right]
        if abs(current_sum) < min_abs_sum:
            # Retain the original exercise's selection behavior.
            min_left = left
            min_right = right
        if current_sum < 0:
            left += 1
        else:
            right -= 1
    print(f"Sum of elements closed to zero are  {arr[min_left],arr[min_right]}")


def sumEquals_givenNumber(arr, k):
    """Print triplets from arr whose sum equals k (in place-sorted input)."""
    bubble_sort(arr)
    numbers_found = False
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == k:
                print(
                    "Three elements whose sum is equal to given number "
                    f"25 are -> {arr[i]},{arr[left]},{arr[right]}"
                )
                numbers_found = True
                break
            elif current_sum < k:
                left += 1
            else:
                right -= 1
    if not numbers_found:
        print("No match found")


def triplets(arr):
    """Print Pythagorean triplets found in arr after sorting it in place."""
    bubble_sort(arr)
    is_triplets = False
    for i in range(len(arr) - 1, 1, -1):
        square = arr[i] * arr[i]
        for left in range(i - 1):
            for right in range(left + 1, i):
                if arr[left] * arr[left] + arr[right] * arr[right] == square:
                    print(
                        f" triplets is given array are -> "
                        f"{arr[left]}, {arr[right]}, {arr[i]}"
                    )
                    is_triplets = True
    if not is_triplets:
        print("No Triplets")


def insertion_sort(arr):
    """Sort ``arr`` in place using insertion sort."""
    for i in range(1, len(arr)):
        value = arr[i]
        j = i
        while j >= 1 and arr[j - 1] > value:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = value
    return arr


def frequency(arr):
    """Print a majority element, or return -1 when none exists."""
    insertion_sort(arr)
    threshold = round(len(arr) / 2)
    final_count = 0
    count = 1
    value = 0
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            count += 1
        else:
            count = 1
        if count > threshold:
            final_count = count
            value = arr[i - 1]
    if final_count > threshold:
        print(
            f"Value {value} appears {final_count} times which is more than "
            f"half the length[{threshold}] of array"
        )
    else:
        return -1


def maximum_zeros(arr, n):
    """Print the row index and zero count for the sorted binary matrix."""
    row = 0
    column = n - 1
    for i in range(n):
        while column >= 0 and arr[i][column] == 0:
            row = i
            column -= 1
    print("Row number = ", row, ", MaxCount = ", n - 1 - column)


def dutuch_flag(arr):
    """Partition 0s, 1s and 2s in place and return the same list."""
    current = 0
    left = 0
    right = len(arr) - 1
    while current < len(arr) and current <= right:
        if arr[current] == 0:
            arr[left], arr[current] = arr[current], arr[left]
            left += 1
            current += 1
        elif arr[current] == 2:
            arr[current], arr[right] = arr[right], arr[current]
            right -= 1
        else:
            current += 1
    return arr
