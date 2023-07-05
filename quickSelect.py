# Very similar to quick sort. But this algorithm is more of a searching algorithm.
# It searches for the kth largest element in an array.

# The way this algorithm works is just the same as quick sort. The only exception is that the end goal is not have a sorted array, but rather
# to find the kth largest element. This means if the current pivot index (pi) is less than k (indexK), then we check the the right side of the 
# pivot index. If the pivot index is greater than k, check the left side of the pivot index. However, if pivot index equals k, then we have found 
# our kth largest element. This strategy of only partitioning one side reduces the time complexity compared to quick sorts, which 
# has to partition both the left and right side.
def quickSelect(array: list[int], k: int):
    #kth largest
    indexK = len(array) - k
    # kth smallest
    # indexK = k - 1
    if indexK < 0:
        print("Illegal Index K: " + str(indexK))
        return -1
    return partition(array, indexK, 0, len(array) - 1)

def partition(array: list[int], k: int, left: int, right: int):
    if left > right:
        return
    pivot = array[right]
    pi = left
    for j in range(left, right, 1):
        if (array[j] <= pivot):
            array[pi], array[j] = array[j], array[pi]
            pi += 1
    array[pi], array[right] = array[right], array[pi]
    if (pi > k):
        return partition(array, k, left, pi - 1)
    elif (pi < k):
        return partition(array, k, pi + 1, right)
    else:
        return array[pi]

def main():
    # array = [17, 21, 12, 12, 21, 10, 3, 6, 14, 7, 4, 8, 12, 19, 12, 9, 4, 12, 2, 1, 3, 15, 21, 0, 20, 11, 7, 8, 10, 19, 0, 16, 12, 14, 1, 17, 15, 6, 4, 3, 18, 17, 11, 3, 18, 9, 5, 8, 4, 9, 9, 6, 7, 4, 5, 6, 6, 3, 13, 16, 19, 16, 19, 8, 12, 4, 17, 16, 6, 3, 2, 12, 2, 20, 16, 5, 15, 18, 16, 17, 18, 3, 9, 15, 15, 14, 2, 1, 15, 7, 15, 10, 1, 17, 6, 8, 21, 9, 19, 18]
    array = [0,1,4,32,90,24,1]
    print("Array: " + str(array))
    k = int(input("K = "))
    ans = quickSelect(array, k)
    print(ans)
main()