import sys


class Node:
    '''
    A LinkedList Node consists of data and a pointer
    to another node
    '''
    def __init__(self, d=None):
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


def fastfunc_reverse_list(LL):
    '''
    Fastfun's linked list reversal
    We reverse a link list by initializing a new head and building
    the list by pushing nodes from the original head to the new head
    '''
    head = LL.getHead()

    # new_head points to nothing at first
    new_head = None

    # traverse will traverse the original list
    traverse = head
    while traverse:
        current = traverse
        traverse = traverse.next
        if new_head:
            current.next = new_head
            new_head = current
        else:
            new_head = current
            new_head.next = None

    LL.setHead(new_head)
    return


def main():
    # Create a list with 5 nodes and print it
    LL = LinkedList()
    for i in range(1, 6):
        n = Node(i)
        LL.append(n)
    sys.stdout.write("Initialized List: ")
    LL.printList()

    # Reverse the linked list
    fastfunc_reverse_list(LL)
    sys.stdout.write("Reversed List: ")
    LL.printList()


if __name__ == "__main__":
    main()
