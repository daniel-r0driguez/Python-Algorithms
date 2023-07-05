# Still need to further understand this algorithm.
def mergeSort(array):
    n = len(array)
    if n > 1:
        mid = n // 2
        arrayOne = []
        arrayTwo = []
        for q in range(0, mid, 1):
            arrayOne.append(array[q])
        for l in range(mid, n, 1):
            arrayTwo.append(array[l])
        mergeSort(arrayOne)
        mergeSort(arrayTwo)
        print(f"Array One: {arrayOne}")
        print(f"Array Two: {arrayTwo}")
        # i is index for arrayOne. j is index for arrayTwo. k is index for array (the array passed through the function)
        i = j = k = 0
        while i < len(arrayOne) and j < len(arrayTwo):
            if arrayOne[i] <= arrayTwo[j]:
                array[k] = arrayOne[i]
                i += 1
            else:
                array[k] = arrayTwo[j]
                j += 1
            k += 1
        # Fill in the remaining elements
        while i < len(arrayOne):
            array[k] = arrayOne[i]
            i += 1
            k += 1
        while j < len(arrayTwo):
            array[k] = arrayTwo[j]
            j += 1
            k += 1
        print(f"Array: {array}")
        print()

def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

if __name__ == '__main__':
    array = [5,1,2,3,4,6,7]
    print("Given array is",end="\n")
    printList(array)
    mergeSort(array)
    print("Sorted array is", end="\n")
    printList(array)

