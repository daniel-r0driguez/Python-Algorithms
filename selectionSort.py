def selectionSort(array):
    for i in range(len(array)):
        minIndex = i
        print("Minimum index = " + str(minIndex))
        for j in range(i + 1, len(array)):
            if array[minIndex] > array[j]:
                minIndex = j
                print("Minimum index now = " + str(minIndex))
        array[i], array[minIndex] = array[minIndex], array[i]
# Stable version of selection sort. Since swapping can cause a loss of order between keys with the same value.
# Example: [4, 5, 2 ,3, 4, 1]. 1 and the first 4 would swap, putting it behind the second 4, making it an unstable sort.
def stableSelectionSort(a):
    # Traverse through all array elements
    for i in range(len(a)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[min_idx] > a[j]:
                min_idx = j
        # Move minimum element at current i
        # Essentially, push all the other
        # elements forward while inserting the minimum index element to where i is.
        key = a[min_idx]
        while min_idx > i:
            a[min_idx] = a[min_idx - 1]
            min_idx -= 1
        a[i] = key

def main():
    array = [0,4,5,1,3,2,8,6,7]
    selectionSort(array)
    print(array)

main()