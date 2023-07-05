# A complete binary tree is one that has all nodes present on each level before the last. On the last level, the nodes are seen from left to right.
# Example: 
#       a       Even thought the last level is not full, the binary tree is still complete since node "d" is present before node "e".
#      / \
#     b   c
#    / \ 
#   d   e
# A full binary tree is one that has all nodes present on each level. A full binary tree is also a complete binary tree.
# Example:
#        a     Each level is filled with the maximum amount of nodes.
#      /   \
#     b     c
#    / \   / \    
#   d   e f   g

# There are two types of heaps. Max heap and min heap
# Max heap is where the parent of the children nodes is greater than its children.
# Min heap is where the parent of the children nodes is less than or equal to its children.
# Formula for representing an array as a binary tree.
# at index i (parent)
# left child of node at index i is (2 * i) + 1 (left child)
# right child of node at index i is (2 * i) + 2 (right child)
# parent of both left and right child is floor(i/2)

# heapify works great. What it does is check if the parent is greater than both of its left and right children. However, if a child is greater than the parent, we swap the two, making the parent the child, and the child the parent. From there, we have to heapify from the former child's position since the parent was less than the child in the first palce.

def heapify(array, N, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if (left < N and array[largest] < array[left]):
        largest = left
    if (right < N and array[largest] < array[right]):
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, N, largest)

def heapSort(array):
    N = len(array)
    # Create the max heap one element at a time.
    for i in range (N//2 - 1, -1, -1):
        heapify(array, N, i)
    print(array)
    # Delete the max heap one element at a time.
    for k in range(N - 1, 0 , -1):
        array[k], array[0] = array[0], array[k]
        heapify(array, k, 0)

def main():
    # array = [8,6,3,10,5,4,9]
    array = [0,1,2,3,4,5,6,7,8,9,10]
    heapSort(array)
    print("Sorted array: " + str(array))

main()