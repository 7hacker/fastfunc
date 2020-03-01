import sys


class Node:
    '''
    A LinkedList Node consists of data and a pointer
    to another node
    '''
    def __init__(self, d=None, double=False):
        self.data = d
        self.next = None
        self.prev = None


class LinkedList:
    '''
    A linkedlist consists of Nodes connected with pointers
    This is a doubly linked list with next and prev pointers
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
        node.prev = None

        self.size = self.size + 1
        if not self.head:
            self.head = node
        else:
            t = self.head
            while t.next:
                t = t.next
            t.next = node
            node.prev = t

    def printList(self):
        t = self.head
        while t.next:
            sys.stdout.write(str(t.data) + "->")
            t = t.next
        sys.stdout.write(str(t.data) + "\n")

    def is_valid(self):
        t = self.head
        forward = ""
        while t.next:
            forward = forward + str(t.data)
            t = t.next
        forward = forward + str(t.data)

        backward = ""
        while t.prev:
            backward = backward + str(t.data)
            t = t.prev
        backward = backward + str(t.data)
        if forward == backward[::-1]:
            return True
        print("Forward Read of list: ", forward)
        print("Backward Read of list: ", backward)
        return False

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
        # Change current's next pointer to point back
        current.next = prev
        # Change current's prev pointer to point forward
        current.prev = forward
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
    print(LL.is_valid())

    # Reverse the linked list - Traditional method
    sys.stdout.write("Reversed List: ")
    reverse_list(LL)
    LL.printList()
    print(LL.is_valid())


if __name__ == "__main__":
    main()
