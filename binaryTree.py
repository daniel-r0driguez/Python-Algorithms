from contextlib import nullcontext

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
    def printTree(self):
        print(self.val)

def main() -> int:
    # Create the nodes
    a = Node("a") #        a
    b = Node("b") #      /   \
    c = Node("c") #     b     c
    d = Node("d") #    / \   / \
    e = Node("e") #   d   e f   g
    f = Node("f") #  / \
    g = Node("g") # h   i
    h = Node("h") #
    i = Node("i")
    # Construct the binary tree using said nodes
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left = h
    d.right = i
    # Perform Breadth-First Search
    print("BFS")
    print("=====")
    BFS(a)
    # Perform Depth-First Search (Left side of tree is priority)
    print("\nDFS")
    print("=====")
    DFS(a)
    print("\n")
    # Find the maximum depth that the tree goes
    maxDepth = maximumDepth(a)
    print(f"\nMax Depth is: {maxDepth}")
    return 0

# BFS uses a queue data structure (first in, first out) which allows for searching through...
# ...a tree horizontally before moving down a level.
def BFS(root):
    queue = [root]
    while queue:
        cur = queue.pop(0)
        if cur == None:
            continue
        print(f"{cur.val} ",end="")
        queue.append(cur.left)
        queue.append(cur.right)

# DFS uses a stack data structure (last in, first out) which allows for searching through a tree vertically...
# ...(right or left side first) before moving to the opposite side.
def DFS(root):
    stack = [root]
    while stack:
        cur = stack.pop()
        if cur == None:
            continue
        print(f"{cur.val} ",end="")
        stack.append(cur.right)
        stack.append(cur.left)

# Since finding the max depth relates heavily to visiting the current level before visiting the next level, BFS...
# ...(queue) is a good algorithm to use. Although DFS works just as well, but may be confusing when printing out...
# ...the current node's value and level.
def maximumDepth(root) -> int:
    depth = 1
    maxDepth = 0
    queue = [[root, depth]]
    while queue:
        cur = queue.pop(0)
        if cur[0] == None:
            continue
        curDepth = cur[1]
        print(f"{cur[0].val} is at level {curDepth}")
        maxDepth = max(maxDepth, curDepth)
        queue.append([cur[0].left, curDepth + 1])
        queue.append([cur[0].right, curDepth + 1])
    return maxDepth
main()
