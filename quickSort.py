from inspect import _void
def main() -> int:
    array = [17, 21, 12, 12, 21, 10, 3, 6, 14, 7, 4, 8, 12, 19, 12, 9, 4, 12, 2, 1, 3, 15, 21, 0, 20, 11, 7, 8, 10, 19, 0, 16, 12, 14, 1, 17, 15, 6, 4, 3, 18, 17, 11, 3, 18, 9, 5, 8, 4, 9, 9, 6, 7, 4, 5, 6, 6, 3, 13, 16, 19, 16, 19, 8, 12, 4, 17, 16, 6, 3, 2, 12, 2, 20, 16, 5, 15, 18, 16, 17, 18, 3, 9, 15, 15, 14, 2, 1, 15, 7, 15, 10, 1, 17, 6, 8, 21, 9, 19, 18]
    partCount = 0
    sortCount = 0
    low = 0
    high = len(array) - 1
    print(f"Unsorted Array: {array}")
    quickSort(array, low, high, partCount, sortCount)
    print("\n")
    print(f"Sorted Array: {array}")
    return 0

def quickSort(array, low, high, partCount, sortCount) -> _void:
    sortCount += 1
    if low < high:
        pi = partition(array, low, high, partCount)
        quickSort(array, low, pi - 1, partCount, sortCount)
        quickSort(array, pi + 1, high, partCount, sortCount)

def partition(array, low, high, partCount) -> int:
    partCount += 1
    # Last element as pivot
    pivot = array[high]
    i = low
    for j in range(low, high, 1):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i

    # First element as pivot
    # pivot = array[low]
    # i = high + 1
    # # On first pass, O(n). On subsequent passes, if a good pivot is chosen, then it is O(log_base2_(n)). Otherwise if the pivot is either the least or greatest item in array, it is O(n^2). i think???
    # for j in range(high, low, -1):
    #     if array[j] > pivot:
    #         i -= 1
    #         array[i], array[j] = array[j], array[i]
    # array[i - 1], array[low] = array[low], array[i - 1]
    # return i - 1

main()