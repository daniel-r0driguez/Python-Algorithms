# The algorithm works by asking one simple question...
# Which is greater? The current element, or the sum of the current element plus the current max that has been found.
# In other words, is the current element greater by itself or as the sum of a sub-array calculated so far.

# If the current element is greater by itself, then that means we are starting the sub-array from that elements index.
# Otherwise if the sum of the element plus the current max (sum of sub-array plus current element) is greater, then that means the element is part 
# of a subarray that started at an earlier index.
# However the current max is not what is returned as the max sum of the sub-array. Instead, a global max is used for this purpose.
# If the current max becomes greater than the global max, the global max is updated to equal the value of the current max and the ending index of 
# the sub-array is updated as well. 
def printSolution(gMax, array, startingIndex, endingIndex):
    if startingIndex == -1:
        startingIndex = 0
    if endingIndex == -1:
        endingIndex = 0
        startingIndex = 0
    if startingIndex > endingIndex:
        startingIndex = endingIndex
    print("===============")
    print(f"The Maximum Subarray Sum is {gMax}.")
    print(f"The Subarray starts at index {startingIndex} and ends at index {endingIndex}.")
    print("Subarray of given array: [", end="")
    for i in range(startingIndex, endingIndex + 1, 1):
        if i == endingIndex:
            print(array[i], end="")
        else:
            print(array[i], end=", ")
    print("]")
    print("===============")
def kadanesAlgo(array):
    gMax = array[0]
    cMax = array[0]
    startingIndex = -1
    endingIndex = -1
    for i in range (1, len(array), 1):
        cMax = max(array[i], cMax + array[i])
        print(cMax)
        if cMax == array[i]:
            startingIndex = i
        if cMax >= gMax:
            endingIndex = i
            gMax = cMax
    printSolution(gMax, array, startingIndex, endingIndex)
if __name__ == '__main__':
    array = [3,1,-5,2,7,19,-9,20,1]
    array2 = [-2, -3, 4, -1, -2, 1, 5, -3]
    array3 = [3,-1, -3,-4,100,2,3,-9,2,-1,99]
    array4 = [1, -1, -1, -1, 2]
    kadanesAlgo(array3)