'''
Not complete!
There should be a fastfunc.com URL here if this code is complete
'''

import sys
from random import randint


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
        '''
        Danger! May not return if its a list with a cycle!
        '''
        t = self.head
        while t.next:
            sys.stdout.write(str(t.data) + "->")
            t = t.next
        sys.stdout.write(str(t.data) + "\n")

    def __len__(self):
        return self.size


def build_list_with_cycle(n):
    '''
    Builds and returns a LinkedList of size n
    '''
    a = randint(1, n)
    counter = 1
    cycle_start_node = None

    LL = LinkedList()
    for i in range(1, n+1):
        n = Node(i)
        LL.append(n)
        if counter == a:
            cycle_start_node = n
        counter = counter + 1

    print("going to set a cycle at node: " + str(a) + " From the last node")
    n.next = cycle_start_node

    return LL


def main():
    # Create a list with 5 nodes and print it
    LL = build_list_with_cycle(13)
    sys.stdout.write("Initialized List: ")
    #LL.printList()


if __name__ == "__main__":
    main()
