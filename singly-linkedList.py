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



if __name__ == '__main__':

    llist = linkedList()
    for x in range(10):
       llist.push(x)
    print(llist)
    print("llist.pop()")
    llist.pop()
    print(llist)
    print("llist.insert(9,10)")
    llist.insert(9,10)
    print(llist)
    print("llist.remove(9)")
    llist.remove(9)
    print(llist)
    print("llist.push(10)")
    llist.push(10)
    print(llist)