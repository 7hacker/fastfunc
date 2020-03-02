import sys


class Node:
    '''
    A LinkedList Node consists of data and a pointer
    to another node
    '''
    def __init__(self, d=None, double=False):
        self.data = d
        self.next = None


class LinkedList:
    '''
    A linkedlist consists of Nodes connected with pointers
    LinkedList head is the first node
    '''
    def __init__(self):
        self.head = None
        self.size = 0

    def getSize(self):
        return self.size

    def getHead(self):
        return self.head

    def setHead(self, node):
        self.head = node

    def append(self, node):
        node.next = None
        self.size = self.size + 1
        if not self.head:
            self.head = node
        else:
            t = self.head
            while t.next:
                t = t.next
            t.next = node

    def printList(self):
        t = self.head
        while t.next:
            sys.stdout.write(str(t.data) + "->")
            t = t.next
        sys.stdout.write(str(t.data) + "\n")

    def __len__(self):
        return self.size


def reverse_list(LL):
    '''
    reverse a list
    Args:
        LL : Linked list object
    '''
    head = LL.getHead()
    current = head
    prev = None
    while current:
        # Forward is used to remember where current should go
        forward = current.next
        # Change current's pointer to point back
        current.next = prev
        # Move prev to current
        prev = current
        # Move current to forward
        current = forward
    LL.setHead(prev)
    return


def build_list(n):
    '''
    Builds and returns a LinkedList of size n
    '''
    LL = LinkedList()
    for i in range(1, n+1):
        n = Node(i)
        LL.append(n)
    return LL


def main():
    # Create a list with 5 nodes and print it
    LL = build_list(5)
    sys.stdout.write("Initialized List: ")
    LL.printList()

    # Reverse the linked list - Traditional method
    sys.stdout.write("Reversed List: ")
    reverse_list(LL)
    LL.printList()


if __name__ == "__main__":
    main()
