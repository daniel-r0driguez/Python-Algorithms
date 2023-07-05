# This is a cycle detection algorithm for Linked Lists
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def printNode(self):
        print(f"Node Value: {self.val}")
        print(f"Next: {self.next.val}")
        print()
    def printLinkedList(self):
        # Check if there is no loop in the list.
        if (floydDetection(self) == True):
            return
        node = self
        while (node.next != None):
            node.printNode()
            node = node.next

# Cycle detection algorithm
def floydDetection(head):
        slow = head
        fast = head
        while (slow != None and fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                print("Error. Linked list has a cycle")
                return True
        return False

def main():
    root = Node(1)
    root.next = Node(2)
    root.next.next = Node(3)
    root.next.next.next = Node(4)
    root.next.next.next.next = Node(5)
    root.next.next.next.next.next = Node(6)
    root.next.next.next.next.next.next = Node(100)
    root.next.next.next.next.next.next.next = root
    root.printLinkedList()
main()