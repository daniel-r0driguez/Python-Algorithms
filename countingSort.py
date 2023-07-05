# Time Complexity: O(n + k)
def countingSort(arr, k):
    # Create count array.
    count = [0] * k # O(k)
    # Create output array.
    output = [0] * len(arr) # O(k) + O(n)
    # Increment count indexes by 1 if they are present in the arr.
    for i in range(0, len(arr), 1): # O(k) + O(2n)
        count[arr[i]] += 1
    print("Count: " + str(count))
    # Get the running sum and store it in count array.
    for i in range(1, k, 1): # O(k) + O(2n) + O(k - 1) 
        count[i] += count[i - 1]
    print(f"Running Sum: {count}")
    # Final for-loop that sorts the items.
    length = len(arr) - 1
    counter = 0
    while length >= 0: # O(k) + O(2n) + O(k - 1) + O(n) = O(3n + 2k - 1) = O(n + k)
        print("length = " + str (length))
        print("arr[length] = " + str(arr[length]))
        print("count[arr[length]] = " + str(count[arr[length]]))
        output[count[arr[length]] - 1] = arr[length]
        print("output[count[arr[length]] - 1] = " + str(output[count[arr[length]] - 1]))
        count[arr[length]] -= 1
        length -= 1
        counter += 1
    return output
    
if __name__ == '__main__':
    array = [9, 0, 2, 3,4, 6,7,2,1,1,0]
    array = countingSort(array, 10)
    print(array)
