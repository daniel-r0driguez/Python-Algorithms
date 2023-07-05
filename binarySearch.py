# Perfect algorithm when you need to perform searches on data that is sorted.
from inspect import _void
def binarySearch(array, targetNumber) -> int:
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + ((right - left) // 2)
        if targetNumber == array[mid]:
            print(f"You number is at index: {mid}")
            return 0
        elif targetNumber > array[mid]:
            left = mid + 1
        else:
            right = mid - 1
    print("That number is not in the array.")
    return 0

def main():
    array = [1,3,5,7,8,95,100,1230,12332]
    targetNumber = int(input("Number you want: "))
    binarySearch(array, targetNumber)
    return 0
main()