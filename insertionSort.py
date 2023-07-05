def insertionSort(array):
    for i in range(1, len(array), 1):
        cur = array[i]
        print("Cur = " + str(cur))
        # Check the previous element, 1 index before cur. 
        j = i - 1
        # Keep checking previous elements until j = - 1 or a smaller element is found.
        while j >= 0 and cur < array[j]:
            print("j = " + str(j))
            array[j + 1] = array[j]
            j -= 1
        # cur's correct index is to right of a smaller number or the beginning of the array if j = -1.
        array[j + 1] = cur

def main():
    array = [8,3,4,5,1,6,2,7]
    insertionSort(array)
    for i in range(len(array)):
        print(array[i], end=" ")

main()