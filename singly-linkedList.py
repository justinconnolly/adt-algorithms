class Node:
    value = 0

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(str(node.value))
            node = node.next

        nodes.append("End")
        return " -> ".join(nodes)

    def push(self, value):
        self.insert(self.length,value)
        return
        self.length += 1

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        node = self.head
        prevNode = node

        while node is not None:
            prevNode = node
            node = node.next

        newNode = Node(value)
        prevNode.next = newNode
        self.tail = newNode

    def pop(self):
        self.remove(self.length - 1)
        return
        if self.length < 1:
            return "Linked List is empty"

        self.length -= 1
        node = self.head
        lastNode = node
        secondLast = lastNode

        while node is not None:
            secondLast = lastNode
            lastNode = node
            node = node.next

        self.tail = secondLast
        secondLast.next = None

    def insert(self, index, value):
        self.length += 1
        newNode = Node(value)

        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return

        node = self.head
        prevNode = node

        for i in range(index):
            prevNode = node
            node = node.next

        newNode.next = node
        prevNode.next = newNode
    
    def remove(self, index):
        if self.length < 1:
            return "Linked List is empty"
            
        if index >= self.length:
            print(f"Index {index} out of bounds (list length is {self.length})")
            return 

        self.length -= 1
        node = self.head
        prevNode = node

        if index == 0:
            self.head = node.next
            node.next = None
            return node.value

        for i in range(index):
            prevNode = node
            node = node.next

        prevNode.next = node.next
        return node.value

    def getHead(self):
        return self.head



def merge(node1: Node, node2: Node) -> Node:
    if node1.value <= node2.value:
        returnHead = node1
        node1 = node1.next
    else:
        returnHead = node2
        node2 = node2.next
        
    currentNode = returnHead

    while node1 is not None and node2 is not None:
        if node1.value <= node2.value:
            currentNode.next = node1
            currentNode = node1
            node1 = node1.next
        else:
            currentNode.next = node2
            currentNode = node2
            node2 = node2.next

    if node1 is not None:
        currentNode.next = node1
    elif node2 is not None:
        currentNode.next = node2

    return returnHead
    
#redundant, was just done in merge()
def mergeHelper(node1: Node, node2: Node, currentNode: Node) -> Node:
    if node1.value <= node2.value:
        currentNode = node1
        node1 = node1.next
    else:
        currentNode = node2
        node2 = node2.next
    return currentNode


def reverse(head: Node):
    pass


if __name__ == '__main__':
    from random import randint
    llist1 = linkedList()
    llist2 = linkedList()
    nextItem = 0
    
    for x in range(1,10):
        prevItem = nextItem
        nextItem += randint(0,2)
        llist1.push(nextItem)
    
    nextItem = 0

    for x in range(randint(1,10)):
        prevItem = nextItem
        nextItem += randint(0,2)
        llist2.push(nextItem)
       
    print(llist1)
    print(llist2)
    node1 = llist1.getHead()
    node2 = llist2.getHead()
    merged = merge(node1,node2)
    while merged is not None:
        print(merged.value, end=" -> ")
        merged = merged.next

    print("End")
